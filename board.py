class Board:
    def __init__(self):
        self.board = None
        self.empty_space = 0
        self.x = None
        self.y = None

    def gen_board(self,x=3, y=3):
        """
        Builds a list of lists 

        Args:
            x: the num of columns the board needs
            y: the num of rows the board needs
        """
        self.board = []
        self.x = x
        self.y = y
        for _ in range(y):
            row = self.make_row(x)
            self.board.append(row)
        self.empty_space = x * y

    def make_row(self,n):
        """
        Builds a list of N length
        """
        row = []
        for _ in range(n):
            row.append(None)
        return row 

    def __len__(self):
        """
        Returns num of board empty spaces
        """
        return self.empty_space

    def get_x_len(self):
        """
        returns len of columns 
        """
        return self.x

    def get_y_len(self):
        """
        returns len of rows 
        """
        return self.y

    def get_row(self,y):
        """
        Returns a row

        Arg:
            y: the index of row we want
        """
        if self.board and y < self.y:
            return self.board[y]
        return None

    def get_col(self,x):
        """
        Returns a col

        Arg: 
            x: the col index we want returned 
        """
        if self.board and x < self.x:
            ret = []
            for r in range(self.y):
                ret.append(self.board[r][x])
            return ret
        return None
    
    def get_square(self,x,y):
        """
        Returns the current value at index

        Arg:
            x: the col index
            y: the row index
        """
        if self.board and x < self.x and y < self.y:
            return self.board[y][x]
        return None

    def set_square(self,x,y,value):
        """
        Sets the current value at index
            if no value decriments empty space

        Arg:
            x: the col index
            y: the row index
            value: the value to insert

        Ret:
            bool if value gets written
        """
        if self.board and x < self.x and y < self.y:
            if not self.board[y][x]:
                self.empty_space -= 1
            self.board[y][x] = value
            return True
        return False

    def print_board(self):
        for row in self.board:
            ret_row = []
            for value in row:
                if value:
                    ret_row.append(value)
                else:
                    ret_row.append(' ')
            print(' '.join(ret_row))
