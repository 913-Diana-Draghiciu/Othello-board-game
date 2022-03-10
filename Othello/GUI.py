import time

import pygame

from Othello import Othello


class Gui:
    def __init__(self, othello):
        self._othello = othello
        pygame.display.set_caption('Othello')

        self._win = pygame.display.set_mode((800, 800))

        self.create_board()
        self.draw_circles()

        pygame.display.update()

    def create_board(self):
        """
        Draws the squares on the board
        :return: -
        """
        self._win.fill((0, 128, 0))
        for i in range(8):
            for j in range(i % 2, 8, 2):
                #(x,y,h,w)
                pygame.draw.rect(self._win, (0, 141, 0), (i * 100, j * 100, 100, 100))

    def draw_circles(self):
        """
        Draws the disks on the board
        :return:
        """
        for i in range(8):
            for j in range(8):
                if self._othello.board[i][j] == 1:
                    # cirlce(loc,color,(x,y),raza,grosime)
                    pygame.draw.circle(self._win, (255, 255, 255), (j * 100 + 100 // 2, i * 100 + 100 // 2), 40, 100)
                if self._othello.board[i][j] == -1:
                    pygame.draw.circle(self._win, (0, 0, 0), (j * 100 + 100 // 2, i * 100 + 100 // 2), 40, 100)

    def determine_winner(self):
        w = 0
        b = 0
        for i in range(8):
            for j in range(8):
                if self._othello.board[i][j] == -1:
                    b += 1
                else:
                    w += 1
                if b > 32:
                    return -1
                if w > 32:
                    return 1
        if b > w:
            return -1
        elif w > b:
            return 1
        else:
            return 0

    def computer_move(self):
        if self._othello.most_strategic_move(1, False) is not None:
            a, b = self._othello.most_strategic_move(1)
            print(str(a)+", "+str(b))
            self._othello.board[a][b] = 1

    def start(self):
        run = True
        while run:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    run = False
                try:
                        if self._othello.most_strategic_move(-1, False) is not None:
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                x = event.pos[1] // 100
                                y = event.pos[0] // 100
                                if self._othello.is_valid(int(x), int(y), -1):
                                    self._othello.board[int(x)][int(y)] = -1
                                    self.computer_move()
                                    self.draw_circles()
                        elif self._othello.most_strategic_move(1, False) is None:
                            run = False
                        else:
                            self.computer_move()
                            self.draw_circles()
                except:
                    continue
            pygame.display.update()
        winner = self.determine_winner()
        if winner == 1:
            print('Computer won!')
        elif winner == -1:
            print('Player won!')
        else:
            print("It's a tie!")
        pygame.quit()


othello = Othello()
gui = Gui(othello)
gui.start()
