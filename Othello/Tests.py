import unittest

# ctrl+shift+f10
from Othello import Othello


class Test(unittest.TestCase):
    def setUp(self):
        self.o = Othello()
        self.o.board[0][2] = 1
        self.o.board[0][3] = 1
        self.o.board[0][4] = 1
        self.o.board[0][5] = 1
        self.o.board[0][6] = 1
        self.o.board[0][7] = 1
        self.o.board[1][2] = -1
        self.o.board[1][3] = 1
        self.o.board[1][4] = -1
        self.o.board[1][5] = 1
        self.o.board[1][7] = -1
        self.o.board[2][0] = -1
        self.o.board[2][1] = -1
        self.o.board[2][2] = -1
        self.o.board[2][3] = -1
        self.o.board[2][4] = -1
        self.o.board[2][5] = -1
        self.o.board[2][6] = -1
        self.o.board[2][7] = -1
        self.o.board[3][0] = 1
        self.o.board[3][2] = -1
        self.o.board[3][3] = 1
        self.o.board[3][4] = -1
        self.o.board[3][5] = -1
        self.o.board[3][6] = -1
        self.o.board[3][7] = -1
        self.o.board[4][2] = -1
        self.o.board[4][3] = -1
        self.o.board[4][4] = -1
        self.o.board[4][5] = -1
        self.o.board[4][6] = 1
        self.o.board[4][7] = -1
        self.o.board[5][2] = -1
        self.o.board[5][3] = 1
        self.o.board[5][4] = -1
        self.o.board[5][5] = 1
        self.o.board[5][7] = -1
        self.o.board[6][2] = -1
        self.o.board[6][4] = 1
        self.o.board[6][5] = -1
        self.o.board[6][7] = -1
        self.o.board[7][2] = -1
        self.o.board[7][3] = 1
        self.o.board[7][4] = 1
        self.o.board[7][5] = 1
        self.o.board[7][6] = 1
        self.o.board[7][7] = 1

    def test_most_strategic_move(self):
        a, b = self.o.most_strategic_move(1, False)
        self.assertEqual(a, 3)
        self.assertEqual(b, 1)

        a, b = self.o.most_strategic_move(-1, False)
        self.assertEqual(a, 4)
        self.assertEqual(b, 0)

    def test_conquer(self):
        self.o.conquer(1, 1, 1, ['ha', 'mda'])
        self.assertEqual(self.o.board[1][2], 1)
        self.assertEqual(self.o.board[2][2], 1)

        self.o.conquer(1, 6, 1, ['va'])
        self.assertEqual(self.o.board[2][6], 1)
        self.assertEqual(self.o.board[3][6], 1)

        self.o.conquer(5, 6, -1, ['hb', 'vb'])
        self.assertEqual(self.o.board[5][5], -1)
        self.assertEqual(self.o.board[4][6], -1)

        self.o.conquer(5, 6, 1, ['sda'])
        self.assertEqual(self.o.board[6][5], 1)

    def test_is_valid(self):
        self.assertEqual(self.o.is_valid(1, 1, 1, False), True)
        self.assertEqual(self.o.is_valid(1, 1, -1, False), False)


if __name__ == '__main__':
    unittest.main()
