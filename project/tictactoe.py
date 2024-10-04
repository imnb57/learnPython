import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QStackedWidget)
from PyQt6.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve
from PyQt6.QtGui import QFont, QIcon, QColor, QPalette

class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe Deluxe")
        self.setFixedSize(QSize(600, 800))
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.scores = {"X": 0, "O": 0, "Ties": 0}
        self.setup_ui()
        self.apply_styles()

    def setup_ui(self):
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        main_layout = QVBoxLayout(central_widget)
        main_layout.setContentsMargins(20, 20, 20, 20)

        self.stacked_widget = QStackedWidget()
        main_layout.addWidget(self.stacked_widget)

        self.create_start_screen()
        self.create_game_screen()
        self.create_end_screen()

        self.stacked_widget.setCurrentIndex(0)

    def create_start_screen(self):
        start_screen = QWidget()
        layout = QVBoxLayout(start_screen)
        layout.setSpacing(20)

        title = QLabel("Tic-Tac-Toe Deluxe")
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setFont(QFont("Montserrat", 36, QFont.Weight.Bold))
        layout.addWidget(title)

        start_button = QPushButton("Start Game")
        start_button.setFixedSize(250, 80)
        start_button.setFont(QFont("Roboto", 18))
        start_button.clicked.connect(lambda: self.stacked_widget.setCurrentIndex(1))
        layout.addWidget(start_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.stacked_widget.addWidget(start_screen)

    def create_game_screen(self):
        game_screen = QWidget()
        layout = QVBoxLayout(game_screen)
        layout.setSpacing(20)

        score_layout = QHBoxLayout()
        self.x_score_label = QLabel("X: 0")
        self.o_score_label = QLabel("O: 0")
        self.tie_score_label = QLabel("Ties: 0")
        for label in (self.x_score_label, self.o_score_label, self.tie_score_label):
            label.setFont(QFont("Roboto", 18))
            score_layout.addWidget(label)
        layout.addLayout(score_layout)

        self.current_player_label = QLabel("Current Player: X")
        self.current_player_label.setFont(QFont("Roboto", 24))
        self.current_player_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(self.current_player_label)

        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(10)
        self.buttons = [[QPushButton("") for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                button.setFixedSize(150, 150)
                button.setFont(QFont("Roboto", 60, QFont.Weight.Bold))
                button.clicked.connect(lambda checked, r=row, c=col: self.on_button_click(r, c))
                self.grid_layout.addWidget(button, row, col)
        layout.addLayout(self.grid_layout)

        self.reset_button = QPushButton("Reset Game")
        self.reset_button.setFixedSize(200, 60)
        self.reset_button.setFont(QFont("Roboto", 16))
        self.reset_button.clicked.connect(self.reset_game)
        layout.addWidget(self.reset_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.stacked_widget.addWidget(game_screen)

    def create_end_screen(self):
        self.end_screen = QWidget()
        layout = QVBoxLayout(self.end_screen)
        layout.setSpacing(20)

        self.result_label = QLabel()
        self.result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.result_label.setFont(QFont("Montserrat", 36, QFont.Weight.Bold))
        layout.addWidget(self.result_label)

        play_again_button = QPushButton("Play Again")
        play_again_button.setFixedSize(250, 80)
        play_again_button.setFont(QFont("Roboto", 18))
        play_again_button.clicked.connect(self.reset_game)
        layout.addWidget(play_again_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.stacked_widget.addWidget(self.end_screen)

    def apply_styles(self):
        # Set color palette
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#f4f4f4"))  # Primary color (60%)
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#2c2c2c"))
        palette.setColor(QPalette.ColorRole.Button, QColor("#4aa3df"))  # Secondary color (30%)
        palette.setColor(QPalette.ColorRole.ButtonText, QColor("#ffffff"))
        palette.setColor(QPalette.ColorRole.Highlight, QColor("#ff9505"))  # Accent color (10%)
        self.setPalette(palette)

        # Apply styles to widgets
        self.setStyleSheet("""
            QPushButton {
                background-color: #4aa3df;
                color: white;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #5cb3ef;
            }
            QPushButton:pressed {
                background-color: #3993cf;
            }
            QLabel {
                color: #2c2c2c;
            }
        """)

        # Style game board buttons separately
        for row in self.buttons:
            for button in row:
                button.setStyleSheet("""
                    QPushButton {
                        background-color: #4dd0e1;
                        color: #2c2c2c;
                        border: 2px solid #4aa3df;
                        border-radius: 10px;
                    }
                    QPushButton:hover {
                        background-color: #5de0f1;
                    }
                    QPushButton:pressed {
                        background-color: #3dc0d1;
                    }
                """)

    def on_button_click(self, row, col):
        if self.buttons[row][col].text() == "":
            self.buttons[row][col].setText(self.current_player)
            self.board[row][col] = self.current_player

            # Animate button press
            self.animate_button_press(self.buttons[row][col])

            if self.check_winner():
                self.show_winner(self.current_player)
            elif self.is_draw():
                self.show_draw()
            else:
                self.switch_player()

    def animate_button_press(self, button):
        animation = QPropertyAnimation(button, b"geometry")
        animation.setDuration(100)
        animation.setEasingCurve(QEasingCurve.Type.OutBack)
        start = button.geometry()
        animation.setStartValue(start)
        animation.setEndValue(start.adjusted(2, 2, -2, -2))
        animation.start()

    def check_winner(self):
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return True
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return True
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return True
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return True
        return False

    def is_draw(self):
        return all(self.board[row][col] != "" for row in range(3) for col in range(3))

    def show_winner(self, player):
        self.scores[player] += 1
        self.update_score_display()
        self.result_label.setText(f"Player {player} wins!")
        self.stacked_widget.setCurrentIndex(2)

    def show_draw(self):
        self.scores["Ties"] += 1
        self.update_score_display()
        self.result_label.setText("It's a draw!")
        self.stacked_widget.setCurrentIndex(2)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.current_player_label.setText(f"Current Player: {self.current_player}")

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText("")
        self.current_player = "X"
        self.current_player_label.setText(f"Current Player: {self.current_player}")
        self.stacked_widget.setCurrentIndex(1)

    def update_score_display(self):
        self.x_score_label.setText(f"X: {self.scores['X']}")
        self.o_score_label.setText(f"O: {self.scores['O']}")
        self.tie_score_label.setText(f"Ties: {self.scores['Ties']}")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())