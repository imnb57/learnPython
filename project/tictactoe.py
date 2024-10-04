import sys
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QVBoxLayout, 
                             QHBoxLayout, QLabel, QStackedWidget, QGraphicsOpacityEffect, QFrame)
from PyQt6.QtCore import Qt, QSize, QPropertyAnimation, QEasingCurve, QTimer, QParallelAnimationGroup
from PyQt6.QtGui import QFont, QColor, QPalette

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
        start_button.clicked.connect(self.start_game)
        layout.addWidget(start_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.stacked_widget.addWidget(start_screen)

    def create_game_screen(self):
        game_screen = QWidget()
        layout = QVBoxLayout(game_screen)
        layout.setSpacing(20)

        # --- Stats Display Section ---
        stats_frame = QFrame()
        stats_frame.setFrameShape(QFrame.Shape.Box)
        stats_frame.setStyleSheet("border-radius: 10px; background-color: #f4f4f4; padding: 15px;")
        stats_layout = QGridLayout(stats_frame)
        stats_layout.setSpacing(20)

        # Score display
        self.x_score_label = QLabel(f"X: {self.scores['X']}")
        self.o_score_label = QLabel(f"O: {self.scores['O']}")
        self.tie_score_label = QLabel(f"Ties: {self.scores['Ties']}")

        # Stylizing score labels
        for label in (self.x_score_label, self.o_score_label, self.tie_score_label):
            label.setFont(QFont("Roboto", 18, QFont.Weight.Bold))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("color: #2c2c2c;")

        stats_layout.addWidget(self.x_score_label, 0, 0, Qt.AlignmentFlag.AlignCenter)
        stats_layout.addWidget(self.o_score_label, 0, 1, Qt.AlignmentFlag.AlignCenter)
        stats_layout.addWidget(self.tie_score_label, 0, 2, Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(stats_frame)

        # --- Current Player Label ---
        self.current_player_label = QLabel(f"Current Player: {self.current_player}")
        self.current_player_label.setFont(QFont("Roboto", 24))
        self.current_player_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.current_player_label.setStyleSheet("color: #4aa3df;")
        layout.addWidget(self.current_player_label)

        # --- Game Board ---
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

        # Reset button
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
        palette.setColor(QPalette.ColorRole.Window, QColor("#f4f4f4"))  # Primary color
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#2c2c2c"))
        palette.setColor(QPalette.ColorRole.Button, QColor("#4aa3df"))  # Secondary color
        palette.setColor(QPalette.ColorRole.ButtonText, QColor("#ffffff"))
        palette.setColor(QPalette.ColorRole.Highlight, QColor("#ff9505"))  # Accent color
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

    def start_game(self):
        self.animate_transition(0, 1)

    def on_button_click(self, row, col):
        if self.buttons[row][col].text() == "":
            self.buttons[row][col].setText(self.current_player)
            self.board[row][col] = self.current_player

            self.animate_button_press(self.buttons[row][col])

            if self.check_winner():
                self.highlight_winning_line()
                QTimer.singleShot(1500, lambda: self.show_winner(self.current_player))
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
        # Check rows, columns, and diagonals for a win
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

    def highlight_winning_line(self):
        winning_line = self.get_winning_line()
        if winning_line:
            for row, col in winning_line:
                button = self.buttons[row][col]
                button.setStyleSheet(button.styleSheet() + "background-color: #ff9505;")

    def get_winning_line(self):
        # Check rows and columns
        for i in range(3):
            if self.board[i][0] == self.board[i][1] == self.board[i][2] != "":
                return [(i, 0), (i, 1), (i, 2)]
            if self.board[0][i] == self.board[1][i] == self.board[2][i] != "":
                return [(0, i), (1, i), (2, i)]
        
        # Check diagonals
        if self.board[0][0] == self.board[1][1] == self.board[2][2] != "":
            return [(0, 0), (1, 1), (2, 2)]
        if self.board[0][2] == self.board[1][1] == self.board[2][0] != "":
            return [(0, 2), (1, 1), (2, 0)]
        
        return None

    def show_winner(self, player):
        self.scores[player] += 1
        self.update_score_display()
        self.result_label.setText(f"Player {player} wins!")
        self.animate_transition(1, 2)

    def show_draw(self):
        self.scores["Ties"] += 1
        self.update_score_display()
        self.result_label.setText("It's a draw!")
        self.animate_transition(1, 2)

    def switch_player(self):
        self.current_player = "O" if self.current_player == "X" else "X"
        self.current_player_label.setText(f"Current Player: {self.current_player}")
        self.animate_player_switch()

    def animate_player_switch(self):
        animation = QPropertyAnimation(self.current_player_label, b"geometry")
        animation.setDuration(300)
        animation.setEasingCurve(QEasingCurve.Type.OutBack)
        start = self.current_player_label.geometry()
        animation.setStartValue(start.adjusted(0, 20, 0, 20))
        animation.setEndValue(start)
        
        opacity_effect = QGraphicsOpacityEffect(self.current_player_label)
        self.current_player_label.setGraphicsEffect(opacity_effect)
        opacity_animation = QPropertyAnimation(opacity_effect, b"opacity")
        opacity_animation.setDuration(300)
        opacity_animation.setStartValue(0)
        opacity_animation.setEndValue(1)
        
        animation_group = QParallelAnimationGroup()
        animation_group.addAnimation(animation)
        animation_group.addAnimation(opacity_animation)
        animation_group.start()

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText("")
                self.buttons[row][col].setStyleSheet(self.buttons[row][col].styleSheet().replace("background-color: #ff9505;", ""))
        self.current_player = "X"
        self.current_player_label.setText(f"Current Player: {self.current_player}")
        self.animate_transition(2, 1)

    def update_score_display(self):
        self.x_score_label.setText(f"X: {self.scores['X']}")
        self.o_score_label.setText(f"O: {self.scores['O']}")
        self.tie_score_label.setText(f"Ties: {self.scores['Ties']}")

    def animate_transition(self, from_index, to_index):
        fade_out = QPropertyAnimation(self.stacked_widget.widget(from_index), b"opacity")
        fade_out.setDuration(300)
        fade_out.setStartValue(1)
        fade_out.setEndValue(0)
        
        fade_in = QPropertyAnimation(self.stacked_widget.widget(to_index), b"opacity")
        fade_in.setDuration(300)
        fade_in.setStartValue(0)
        fade_in.setEndValue(1)
        
        transition_group = QParallelAnimationGroup()
        transition_group.addAnimation(fade_out)
        transition_group.addAnimation(fade_in)
        
        self.stacked_widget.setCurrentIndex(to_index)
        self.stacked_widget.widget(from_index).setGraphicsEffect(QGraphicsOpacityEffect())
        self.stacked_widget.widget(to_index).setGraphicsEffect(QGraphicsOpacityEffect())
        
        transition_group.start()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle("Fusion")
    window = TicTacToe()
    window.show()
    sys.exit(app.exec())