import sys
import numpy as np
import json
import random
from PyQt6.QtWidgets import (QApplication, QMainWindow, QPushButton, QGridLayout, QWidget, QVBoxLayout,
                             QHBoxLayout, QLabel, QStackedWidget, QGraphicsOpacityEffect, QFrame)
from PyQt6.QtCore import Qt, QSize, QTimer
from PyQt6.QtGui import QFont, QColor, QPalette


class TicTacToeAI:
    def __init__(self, player):
        self.player = player
        self.q_table = {}
        self.learning_rate = 0.1
        self.discount_factor = 0.95
        self.epsilon = 0.1
        self.load_q_table()

    def get_state(self, board):
        return ''.join([''.join(row) for row in board])

    def get_available_actions(self, board):
        return [(r, c) for r in range(3) for c in range(3) if board[r][c] == ""]

    def choose_action(self, board):
        state = self.get_state(board)
        if random.random() < self.epsilon:
            return random.choice(self.get_available_actions(board))
        else:
            q_values = self.q_table.get(state, {})
            if not q_values:
                return random.choice(self.get_available_actions(board))
            return max(q_values, key=q_values.get)

    def update_q_table(self, state, action, next_state, reward):
        if state not in self.q_table:
            self.q_table[state] = {}
        action_key = f"{action[0]},{action[1]}"  # Convert tuple to string
        if action_key not in self.q_table[state]:
            self.q_table[state][action_key] = 0

        old_q_value = self.q_table[state][action_key]
        next_max_q_value = max(self.q_table.get(next_state, {}).values() or [0])

        new_q_value = old_q_value + self.learning_rate * (reward + self.discount_factor * next_max_q_value - old_q_value)
        self.q_table[state][action_key] = new_q_value

    def decide_move(self, board):
        return self.choose_action(board)

    def load_q_table(self):
        try:
            with open("q_table.json", "r") as f:
                self.q_table = json.load(f)
                # Convert action keys back to tuples
                for state in self.q_table:
                    self.q_table[state] = {tuple(map(int, action.split(','))): q_value for action, q_value in self.q_table[state].items()}
        except (FileNotFoundError, json.JSONDecodeError):
            self.q_table = {}

    def save_q_table(self):
        # Convert action tuples to strings for saving
        q_table_to_save = {
            state: {f"{action[0]},{action[1]}": q_value for action, q_value in actions.items()}
            for state, actions in self.q_table.items()
        }
        with open("q_table.json", "w") as f:
            json.dump(q_table_to_save, f)


class TicTacToe(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Tic-Tac-Toe Deluxe")
        self.setFixedSize(QSize(600, 800))
        self.current_player = "X"
        self.board = [["" for _ in range(3)] for _ in range(3)]
        self.scores = {"X": 0, "O": 0, "Ties": 0}
        self.ai = TicTacToeAI(player="O")
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

        train_button = QPushButton("Train AI")
        train_button.setFixedSize(250, 80)
        train_button.setFont(QFont("Roboto", 18))
        train_button.clicked.connect(self.train_ai)
        layout.addWidget(train_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.stacked_widget.addWidget(start_screen)

    def create_game_screen(self):
        game_screen = QWidget()
        layout = QVBoxLayout(game_screen)
        layout.setSpacing(20)

        # Stats Display Section
        stats_frame = QFrame()
        stats_frame.setFrameShape(QFrame.Shape.Box)
        stats_frame.setStyleSheet("border-radius: 10px; background-color: #f4f4f4; padding: 15px;")
        stats_layout = QGridLayout(stats_frame)
        stats_layout.setSpacing(20)

        self.x_score_label = QLabel(f"X: {self.scores['X']}")
        self.o_score_label = QLabel(f"O: {self.scores['O']}")
        self.tie_score_label = QLabel(f"Ties: {self.scores['Ties']}")

        for label in (self.x_score_label, self.o_score_label, self.tie_score_label):
            label.setFont(QFont("Roboto", 18, QFont.Weight.Bold))
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            label.setStyleSheet("color: #2c2c2c;")

        stats_layout.addWidget(self.x_score_label, 0, 0, Qt.AlignmentFlag.AlignCenter)
        stats_layout.addWidget(self.o_score_label, 0, 1, Qt.AlignmentFlag.AlignCenter)
        stats_layout.addWidget(self.tie_score_label, 0, 2, Qt.AlignmentFlag.AlignCenter)

        layout.addWidget(stats_frame)

        # Current Player Label
        self.current_player_label = QLabel(f"Current Player: {self.current_player}")
        self.current_player_label.setFont(QFont("Roboto", 24))
        self.current_player_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.current_player_label.setStyleSheet("color: #4aa3df;")
        layout.addWidget(self.current_player_label)

        # Game Board
        self.grid_layout = QGridLayout()
        self.grid_layout.setSpacing(10)
        self.buttons = [[QPushButton("") for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                button = self.buttons[row][col]
                button.setFixedSize(150, 150)
                button.setFont(QFont("Roboto", 60, QFont.Weight.Bold))
                button.clicked.connect(lambda checked, r=row, c=col: self.player_move(r, c))
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
        play_again_button.clicked.connect(self.play_again)
        layout.addWidget(play_again_button, alignment=Qt.AlignmentFlag.AlignCenter)

        self.stacked_widget.addWidget(self.end_screen)

    def apply_styles(self):
        palette = QPalette()
        palette.setColor(QPalette.ColorRole.Window, QColor("#f4f4f4"))
        palette.setColor(QPalette.ColorRole.WindowText, QColor("#2c2c2c"))
        palette.setColor(QPalette.ColorRole.Button, QColor("#4aa3df"))
        palette.setColor(QPalette.ColorRole.ButtonText, QColor("#ffffff"))
        palette.setColor(QPalette.ColorRole.Highlight, QColor("#ff9505"))
        self.setPalette(palette)

        self.setStyleSheet("""        
            QPushButton {
                background-color: #4aa3df;
                color: white;
                border: none;
                border-radius: 10px;
            }
            QPushButton:hover {
                background-color: #3a8bc9;
            }
        """)

    def start_game(self):
        self.reset_game()
        self.stacked_widget.setCurrentIndex(1)
        self.current_player = "X"  # X always goes first
        self.current_player_label.setText(f"Current Player: {self.current_player}")

    def reset_game(self):
        self.board = [["" for _ in range(3)] for _ in range(3)]
        for row in range(3):
            for col in range(3):
                self.buttons[row][col].setText("")
                self.buttons[row][col].setEnabled(True)
        self.x_score_label.setText(f"X: {self.scores['X']}")
        self.o_score_label.setText(f"O: {self.scores['O']}")
        self.tie_score_label.setText(f"Ties: {self.scores['Ties']}")
        self.current_player = "X"
        self.current_player_label.setText(f"Current Player: {self.current_player}")

    def player_move(self, row, col):
        if self.board[row][col] == "":
            self.board[row][col] = self.current_player
            self.buttons[row][col].setText(self.current_player)
            self.buttons[row][col].setEnabled(False)
            if self.check_winner(self.current_player):
                self.end_game(f"Player {self.current_player} wins!")
            elif all(cell != "" for row in self.board for cell in row):
                self.end_game("It's a tie!")
            else:
                self.current_player = "O"
                self.current_player_label.setText(f"Current Player: {self.current_player}")
                self.ai_move()

    def ai_move(self):
        available_actions = self.ai.get_available_actions(self.board)
        state = self.ai.get_state(self.board)

        if available_actions:
            action = self.ai.decide_move(self.board)
            self.board[action[0]][action[1]] = self.current_player
            self.buttons[action[0]][action[1]].setText(self.current_player)
            self.buttons[action[0]][action[1]].setEnabled(False)

            if self.check_winner(self.current_player):
                self.end_game(f"Player {self.current_player} wins!")
            elif all(cell != "" for row in self.board for cell in row):
                self.end_game("It's a tie!")
            else:
                self.current_player = "X"
                self.current_player_label.setText(f"Current Player: {self.current_player}")

        next_state = self.ai.get_state(self.board)
        reward = 0

        if self.check_winner(self.current_player):
            reward = 1  # AI wins
        elif all(cell != "" for row in self.board for cell in row):
            reward = 0.5  # Tie
        self.ai.update_q_table(state, action, next_state, reward)

    def check_winner(self, player):
        # Check rows, columns, and diagonals for a win
        for r in range(3):
            if all(self.board[r][c] == player for c in range(3)):
                return True
        for c in range(3):
            if all(self.board[r][c] == player for r in range(3)):
                return True
        if all(self.board[i][i] == player for i in range(3)) or all(self.board[i][2 - i] == player for i in range(3)):
            return True
        return False

    

    def end_game(self, message):
     self.result_label.setText(message)
     self.stacked_widget.setCurrentIndex(2)

    # Correctly extract the winner's identifier
     winner = message.split()[1]  # This will give you "X" or "O"

     if winner in self.scores:
        self.scores[winner] += 1

     self.x_score_label.setText(f"X: {self.scores['X']}")
     self.o_score_label.setText(f"O: {self.scores['O']}")
     self.tie_score_label.setText(f"Ties: {self.scores['Ties']}")


    def play_again(self):
        self.reset_game()
        self.stacked_widget.setCurrentIndex(1)

    def train_ai(self):
        # Training routine could go here, not implemented in this example
        self.ai.save_q_table()
        print("Training completed and Q-table saved.")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    game = TicTacToe()
    game.show()
    sys.exit(app.exec())
