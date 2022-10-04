"""tests"""
import unittest
import tic_tac


class TestTicTac(unittest.TestCase):
    """test class"""

    def setUp(self) -> None:
        """Set up test"""
        self.game = tic_tac.TicTac()

    def test_check_win(self):
        """Test for check_win for boards
        X X X
        0 0 6
        7 8 9

        X X 3
        0 0 6
        7 8 9

        X X 0
        0 0 X
        X 0 X"""
        self.game.board = ['X', 'X', 'X', '0', '0', 6, 7, 8, 9]
        self.assertTrue(self.game.check_win('X'), print("Должен быть победитель для \nX X X\nO O 6\n7 8 9"))
        self.game.board = ['X', 'X', '3', '0', '0', 6, 7, 8, 9]
        self.assertFalse(self.game.check_win('X'), print("Не должно быть победителя для \nX X 3\nO O 6\n7 8 9"))
        self.game.board = ['X', 'X', '0', '0', '0', 'X', 'X', '0', 'X']
        self.assertFalse(self.game.check_win('0'), print("Не должно быть победителя для \nX X 0\nO O X\nX 0 X"))

    def test_check_tie(self):
        """Test for tie for boards
        X X 0
        0 0 X
        X 0 X

        X X X
        0 0 6
        7 8 9"""
        self.game.board = ['X', 'X', '0', '0', '0', 'X', 'X', '0', 'X']
        self.assertTrue(self.game.check_tie(), print("Ничья для доски \nX X 0\nO O X\nX 0 X"))
        self.game.board = ['X', 'X', 'X', '0', '0', 6, 7, 8, 9]
        self.assertFalse(self.game.check_tie(), print("Нет ничьей для доски \nX X X\nO O 6\n7 8 9"))

    def test_input_validation_positiv(self):
        """Test for valide input 1...9"""
        for i in range(9):
            self.game.board = [1, 2, 3, 4, 5, 6, 7, 8, 9]
            self.game.validate_input(i+1)


if __name__ == '__main__':
    test = TestTicTac()
    test.test_check_win()
    test.test_check_tie()
    test.test_input_validation_positiv()