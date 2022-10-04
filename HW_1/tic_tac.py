"""TicTac game"""
import random


class TicTac:
    """Tic Tac"""

    def __init__(self):
        """init func"""
        self.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        self.numbers = {1, 2, 3, 4, 5, 6, 7, 8, 9}
        self.human = ''
        self.a_i = ''
        self.ways_to_win = ((0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6))

    def minimax(self, depth, is_max):
        """Minimax algo"""
        if self.check_win(self.a_i):
            return 1
        if self.check_win(self.human):
            return -1
        if self.check_tie():
            return 0
        if is_max:
            best_score = -800
            for i in range(0, 9):
                if self.board[i] in self.numbers:
                    self.board[i] = self.a_i
                    score = self.minimax(depth + 1, False)
                    self.board[i] = i + 1
                    if score > best_score:
                        best_score = score
            return best_score
        else:
            best_score = 800
            for i in range(0, 9):
                if self.board[i] in self.numbers:
                    self.board[i] = self.human
                    score = self.minimax(depth + 1, True)
                    self.board[i] = i + 1
                    if score < best_score:
                        best_score = score
            return best_score

    def comp_move(self):
        """The computer chooses its move"""
        best_score = -1000
        best_move = 0
        for i in range(0, 9):
            if self.board[i] in self.numbers:
                self.board[i] = self.a_i
                score = self.minimax(0, False)
                self.board[i] = i + 1
                if score > best_score:
                    best_score = score
                    best_move = i
        self.board[best_move] = self.a_i
        print('Компьютер сделал ход')
        self.show_board()

    def check_win(self, player):
        """Checks win"""
        for row in self.ways_to_win:
            if self.board[row[0]] == self.board[row[1]] == self.board[row[2]] == player:
                return True
        return False

    def check_tie(self):
        """Checks tie"""
        for i in range(9):
            if self.board[i] in self.numbers:
                return False
        return True

    def validate_input(self, choice):
        """Validates input"""
        print('Введите цифру от 1 до 9 для выбора ячейки')
        while True:
            try:
                if choice in self.numbers:
                    if self.board[choice - 1] != 'X' or self.board[choice - 1] != '0':
                        print('Вы сделали ход')
                        break
                    print('Эта ячейка уже занята. Пожалуйста, выберите другую')
                else:
                    print('Вы уверены, что ввели число от 1 до 9? Пожалуйста, повторите попытку')
            except ValueError:
                print('Ошибка значения. Вы уверены, что ввели число от 1 до 9? Пожалуйста, повторите попытку')
                continue
        self.board[choice - 1] = self.human
        self.show_board()

    def show_board(self):
        """Prints board"""
        print("-------------")
        for i in range(3):
            print("|", self.board[0 + i * 3], "|", self.board[1 + i * 3], "|", self.board[2 + i * 3], "|")
            print("-------------")

    def start_game(self):
        """Starts game"""
        print('Привет! Вы играете в "Крестики-нолики". Хотите играть за крестики или за нолики? Введите 0 или Х')
        try:
            while True:
                turn = input()
                if turn in {'х', 'Х', 'x',  'X'}:
                    self.human = 'X'
                    self.a_i = '0'
                    break
                if turn in {'o', 'O', '0',  'о', 'О'}:
                    self.a_i = 'X'
                    self.human = '0'
                    break
                print('Пожалуйста, введите корректное значение')
        except ValueError:
            print('Ошибка значения. Пожалуйста, введите корректное значение')
        if self.a_i == 'X':
            print('Компьютер сделал ход')
            self.board[random.randint(0, 8)] = 'X'
        self.show_board()
        while True:
            print('Введите цифру от 1 до 9 для выбора ячейки')
            choice = int(input())
            self.validate_input(choice)
            if self.check_win(self.human):
                print('Человек победил...жаль, что это невозможно')
                break
            if self.check_tie():
                print('Ничья')
                break
            self.comp_move()
            if self.check_win(self.a_i):
                print('Победил компьютер')
                break
            if self.check_tie():
                print('Ничья')
                break


if __name__ == '__main__':
    game = TicTac()
    game.start_game()
