from Othello import Othello


class UI:
    def __init__(self, Othello):
        self.o = Othello
        self.init_board()

    def init_board(self):
        self.o.board[0][0] = 1
        self.o.board[0][1] = -1
        self.o.board[0][2] = 1
        self.o.board[0][3] = 1
        self.o.board[0][4] = 1
        self.o.board[0][5] = 1
        self.o.board[0][6] = 1
        self.o.board[0][7] = 1

        self.o.board[1][0] = -1
        self.o.board[1][1] = 1
        self.o.board[1][2] = 1
        self.o.board[1][3] = 1
        self.o.board[1][4] = 1
        self.o.board[1][5] = 1
        self.o.board[1][6] = 1
        self.o.board[1][7] = -1

        self.o.board[2][0] = -1
        self.o.board[2][1] = 1
        self.o.board[2][2] = 1
        self.o.board[2][3] = 1
        self.o.board[2][4] = 1
        self.o.board[2][5] = -1
        self.o.board[2][6] = 1
        self.o.board[2][7] = -1

        self.o.board[3][0] = -1
        self.o.board[3][1] = 1
        self.o.board[3][2] = 1
        self.o.board[3][3] = 1
        self.o.board[3][4] = -1
        self.o.board[3][5] = 1
        self.o.board[3][6] = 1
        self.o.board[3][7] = -1

        self.o.board[4][0] = -1
        self.o.board[4][1] = 1
        self.o.board[4][2] = 1
        self.o.board[4][3] = 1
        self.o.board[4][4] = 1
        self.o.board[4][5] = -1
        self.o.board[4][6] = 1
        self.o.board[4][7] = -1

        self.o.board[5][0] = -1
        self.o.board[5][1] = -1
        self.o.board[5][2] = -1
        self.o.board[5][3] = -1
        self.o.board[5][4] = -1
        self.o.board[5][5] = -1
        self.o.board[5][6] = -1
        self.o.board[5][7] = -1

        self.o.board[6][0]=-1
        self.o.board[6][7] = -1


    @staticmethod
    def print_instructions():
        print(
            "There are sixty-four identical game pieces called disks. Players take turns placing disks on the board with their assigned color. During a play, any disks of the opponent's color that are in a straight line (horizontally, vertically and diagonally) and bounded by the disk just placed and another disk of the current player's color are turned over to the current player's color. The object of the game is to have the majority of disks turned to display your color when the last playable empty square is filled.")

    def print_board(self):
        print(str(self.o))

    def determine_winner(self):
        w = 0
        b = 0
        for i in range(8):
            for j in range(8):
                if self.o.board[i][j] == -1:
                    b += 1
                else:
                    w += 1
                if b > 32:
                    print("Black won!")
                    return
                if w > 32:
                    print("White won!")
                    return
        if b > w:
            print("Black won!")
        elif w > b:
            print("White won!")
        else:
            print("It's a tie!")

    def computer_mode(self):
        """
        Player always starts first, having the disk color black
        :return:
        """
        disk_turn = -1
        while True:
            if disk_turn == -1:
                if self.o.most_strategic_move(-1, False) is not None:
                    player_placement = input("player: ")
                    player_placement = player_placement.split(",")
                    while not self.o.is_valid(int(player_placement[0]), int(player_placement[1]), -1):
                        print("Move not valid!")
                        player_placement = input("player: ")
                        player_placement = player_placement.split(",")

                    self.o.board[int(player_placement[0])][int(player_placement[1])] = -1
                    self.print_board()
                    disk_turn = 1
                elif self.o.most_strategic_move(1, False) is None:
                    self.determine_winner()
                    break
                else:
                    print("There are no more valid moves for you left!")
                    disk_turn = 1
            else:
                if self.o.most_strategic_move(1, False) is None:
                    if self.o.most_strategic_move(-1, False) is not None:
                        disk_turn = -1
                        print("The computer has no valid moves to make, it's your turn!")
                    else:
                        self.determine_winner()
                        break
                else:
                    a, b = self.o.most_strategic_move(1)
                    self.o.board[a][b] = 1
                    print(str(a)+", "+str(b))
                    self.print_board()
                    disk_turn = -1

    def two_player_mode(self):
        disk_turn = -1
        while True:
            if disk_turn == -1:
                if self.o.most_strategic_move(-1, False) is not None:
                    player_placement = input("Black: ")
                    player_placement = player_placement.split(",")
                    while not self.o.is_valid(int(player_placement[0]), int(player_placement[1]), -1):
                        print("Move not valid!")
                        player_placement = input("Black: ")
                        player_placement = player_placement.split(",")

                    self.o.board[int(player_placement[0])][int(player_placement[1])] = -1
                    self.print_board()
                    disk_turn = 1
                elif self.o.most_strategic_move(1, False) is None:
                    self.determine_winner()
                    break
                else:
                    print("There are no more valid moves for player-black left!")
                    disk_turn = 1
            else:
                if self.o.most_strategic_move(1, False) is None:
                    if self.o.most_strategic_move(-1, False) is not None:
                        disk_turn = -1
                        print("There are no more valid moves left for player-white!")
                    else:
                        self.determine_winner()
                        break
                else:
                    player_placement = input("White: ")
                    player_placement = player_placement.split(",")
                    while not self.o.is_valid(int(player_placement[0]), int(player_placement[1]), 1):
                        print("Move not valid!")
                        player_placement = input("White: ")
                        player_placement = player_placement.split(",")

                    self.o.board[int(player_placement[0])][int(player_placement[1])] = 1
                    self.print_board()
                    disk_turn = -1

    def menu(self):
        self.print_instructions()

        computer = input("Enter 1 - for 1 player mode (vs. computer) or 2 - for 2 players: ")
        try:
            self.print_board()
            if int(computer) == 1:
                try:
                    self.computer_mode()
                except ValueError as va:
                    print(va)
            elif int(computer) == 2:
                try:
                    self.two_player_mode()
                except ValueError as va:
                    print(va)
            else:
                raise ValueError("Input not correct! Please enter key 1 or 2!")
        except ValueError as va:
            print(va)


o = Othello()
ui = UI(o)
ui.menu()
