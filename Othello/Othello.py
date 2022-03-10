from texttable import Texttable


class Othello:
    def __init__(self):
        # init board with zero
        self.__board = [0] * 8
        for i in range(8):
            self.__board[i] = [0] * 8

        # init black disks (negative)
        self.__board[3][3] = -1
        self.__board[4][4] = -1

        # init white disks (positive)
        self.__board[3][4] = 1
        self.__board[4][3] = 1

    def __setitem__(self, key, value):
        self.board[key] = value

    @property
    def board(self):
        return self.__board

    @board.setter
    def board(self, index1, index2, value):
        self.board[index1][index2] = value

    def most_strategic_move(self, disk_type, change=True):
        """
        Checks if there is possible move in any of the 4 corners, if not
        Checks if there is a possible move on the exterior frame of the board, else
        Avoids the frame of the corners, unless the diagonal is yours
        Checks if there is a possible move in the central 4x4 board, more explicit lines 2-5 and columns, else
        Checks if there is a possible move which isn't the inner-exterior frame (line and column 1), else
        Returns any move left
        if none left, the other player must make the next move

        Keep your pieces grouped together to minimise your opponents moves
        :return: The most strategic placement of a disk
        """
        # corners
        if self.is_valid(0, 0, disk_type, change):
            return 0, 0
        elif self.is_valid(7, 7, disk_type, change):
            return 7, 7
        elif self.is_valid(0, 7, disk_type, change):
            return 0, 7
        elif self.is_valid(7, 0, disk_type, change):
            return 7, 0

        # vertical exterior frame (except corner frame)
        for i in range(2, 6):
            if self.is_valid(i, 0, disk_type, change):
                return i, 0
            if self.is_valid(i, 7, disk_type, change):
                return i, 7

        # horizontal exterior frame (except corner frame)
        for j in range(2, 6):
            if self.is_valid(0, j, disk_type, change):
                return 0, j
            if self.is_valid(7, j, disk_type, change):
                return 7, j

        # move in central 4x4 board
        for i in range(2, 6):
            for j in range(2, 6):
                if self.is_valid(i, j, disk_type, change):
                    return i, j

        # move on inner frame except corner frame
        for i in range(1, 7):
            for j in range(1, 7):
                if ((i < 2 or i > 5) or (j < 2 or j < 5)) and (i != 1 or j != 1) and (i != 1 or j != 6) and (
                        i != 6 or j != 1) and (i != 6 or j != 6):
                    if self.is_valid(i, j, disk_type, change):
                        return i, j

        # corner frame
        if self.is_valid(0, 1, disk_type, change):
            return 0, 1
        elif self.is_valid(1, 0, disk_type, change):
            return 1, 0
        elif self.is_valid(0, 6, disk_type, change):
            return 0, 6
        elif self.is_valid(6, 0, disk_type, change):
            return 6, 0
        elif self.is_valid(1, 7, disk_type, change):
            return 1, 7
        elif self.is_valid(7, 1, disk_type, change):
            return 7, 1
        elif self.is_valid(7, 6, disk_type, change):
            return 7, 6
        elif self.is_valid(6, 7, disk_type, change):
            return 6, 7
        elif self.is_valid(1, 1, disk_type, change):
            return 1, 1
        elif self.is_valid(6, 6, disk_type, change):
            return 6, 6
        elif self.is_valid(1, 6, disk_type, change):
            return 1, 6
        elif self.is_valid(6, 1, disk_type, change):
            return 6, 1

        return None

    def conquer(self, pos_line, pos_column, disk_type, conquers_list):
        """
        Changes the disks on the board according to the conquer list
        :param pos_line:
        :param pos_column:
        :param disk_type:
        :param conquers_list:
        :return:
        """
        if "ha" in conquers_list:
            j = pos_column + 1
            while self.board[pos_line][j] != disk_type:
                self.board[pos_line][j] = disk_type
                j += 1

        if "hb" in conquers_list:
            j = pos_column - 1
            while self.board[pos_line][j] != disk_type:
                self.board[pos_line][j] = disk_type
                j -= 1

        if "va" in conquers_list:
            i = pos_line + 1
            while self.board[i][pos_column] != disk_type:
                self.board[i][pos_column] = disk_type
                i += 1

        if "vb" in conquers_list:
            i = pos_line - 1
            while self.board[i][pos_column] != disk_type:
                self.board[i][pos_column] = disk_type
                i -= 1

        if "mda" in conquers_list:
            i = pos_line + 1
            j = pos_column + 1
            while self.board[i][j] != disk_type:
                self.board[i][j] = disk_type
                i += 1
                j += 1

        if "mdb" in conquers_list:
            i = pos_line - 1
            j = pos_column - 1
            while self.board[i][j] != disk_type:
                self.board[i][j] = disk_type
                i -= 1
                j -= 1

        if "sda" in conquers_list:
            i = pos_line + 1
            j = pos_column - 1
            while self.board[i][j] != disk_type:
                self.board[i][j] = disk_type
                i += 1
                j -= 1

        if "sdb" in conquers_list:
            i = pos_line - 1
            j = pos_column + 1
            while self.board[i][j] != disk_type:
                self.board[i][j] = disk_type
                i -= 1
                j += 1

    def is_valid(self, pos_line, pos_column, disk_type, change=True):
        """
        Checks if the given position on the board is correct and returns True if so
        :param pos_line:
        :param pos_column:
        :param disk_type:
        :return: True if position is validated or False otherwise
        """
        conquers = []
        # checks if position on board is empty
        if self.board[pos_line][pos_column] != 0:
            return False

        # check horizontally after pos location
        for j in range(pos_column + 1, 8):
            if self.board[pos_line][j] == 0:
                break
            if self.board[pos_line][j] == disk_type and self.board[pos_line][j - 1] != disk_type and \
                    self.board[pos_line][j - 1] != 0:
                if change is False:
                    return True
                conquers.append("ha")
                break
            elif self.board[pos_line][j] == disk_type:
                break

        # check horizontally before pos location
        for j in range(pos_column - 1, 0, -1):
            if self.board[pos_line][j] == 0:
                break
            if self.board[pos_line][j] == disk_type and self.board[pos_line][j + 1] != disk_type and \
                    self.board[pos_line][j + 1] != 0:
                if change is False:
                    return True
                conquers.append("hb")
                break
            elif self.board[pos_line][j] == disk_type:
                break

        # check vertically after pos location
        for i in range(pos_line + 1, 8):
            if self.board[i][pos_column] == 0:
                break
            if self.board[i][pos_column] == disk_type and self.board[i - 1][pos_column] != disk_type and \
                    self.board[i - 1][pos_column] != 0:
                if change is False:
                    return True
                conquers.append("va")
                break
            elif self.board[i][pos_column] == disk_type:
                break

        # check vertically before pos location
        for i in range(pos_line - 1, 0, -1):
            if self.board[i][pos_column] == 0:
                break
            if self.board[i][pos_column] == disk_type and self.board[i + 1][pos_column] != disk_type and \
                    self.board[i + 1][pos_column] != 0:
                if change is False:
                    return True
                conquers.append("vb")
                break
            elif self.board[i][pos_column] == disk_type:
                break

        # check on the main diagonal after pos location
        i = pos_line + 1
        j = pos_column + 1
        while i < 8 and j < 8:
            if self.board[i][j] == 0:
                break
            if self.board[i][j] == disk_type and self.board[i - 1][j - 1] != disk_type and self.board[i - 1][
                j - 1] != 0:
                if change is False:
                    return True
                conquers.append("mda")
                break
            elif self.board[i][j] == disk_type:
                break
            i += 1
            j += 1

        # check on the main diagonal before pos location
        i = pos_line - 1
        j = pos_column - 1
        while i >= 0 and j >= 0:
            if self.board[i][j] == 0:
                break
            if self.board[i][j] == disk_type and self.board[i + 1][j + 1] != disk_type and self.board[i + 1][
                j + 1] != 0:
                if change is False:
                    return True
                conquers.append("mdb")
                break
            elif self.board[i][j] == disk_type:
                break
            i -= 1
            j -= 1

        # check on the secondary diagonal after pos
        i = pos_line + 1
        j = pos_column - 1
        while i < 8 and j >= 0:
            if self.board[i][j] == 0:
                break
            if self.board[i][j] == disk_type and self.board[i - 1][j + 1] != disk_type and self.board[i - 1][
                j + 1] != 0:
                if change is False:
                    return True
                conquers.append("sda")
                break
            elif self.board[i][j] == disk_type:
                break
            i += 1
            j -= 1

        # check on the secondary diagonal before pos
        i = pos_line - 1
        j = pos_column + 1
        while j < 8 and i >= 0:
            if self.board[i][j] == 0:
                break
            if self.board[i][j] == disk_type and self.board[i + 1][j - 1] != disk_type and self.board[i + 1][
                j - 1] != 0:
                if change is False:
                    return True
                conquers.append("sdb")
                break
            elif self.board[i][j] == disk_type:
                break
            i -= 1
            j += 1

        if len(conquers) != 0:
            if change is True:
                self.conquer(pos_line, pos_column, disk_type, conquers)
            return True

        return False

    def __str__(self):
        t = Texttable()
        t.header(['', 0, 1, 2, 3, 4, 5, 6, 7])

        for row in range(0, 8):
            aux = []
            for elem in self.board[row]:
                if elem == 1:
                    aux.append('🖤')
                elif elem == -1:
                    aux.append("〇")
                else:
                    aux.append('')
            t.add_row([row] + aux)
        return t.draw()
