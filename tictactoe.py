from board import Board
from player import PlayerQue

class TicTacToe(Board):
    def __init__(self):
        self.board = None
        self.players = None

    def setup(self):
        """
        Creates Player que and the board

        """
        self.players = PlayerQue()
        self.players.add_players()
        self.players.make_turn_order()
        self.gen_board(3,3)
        
    def intro(self):
        print('Welcome to Tic Tac Toe')

    def outro(self):
        print('Would you like to play again?')
        answer = input()
        if answer.lower() == 'yes':
            print('awesome recursive call')
        else:
            print('Thank you for playing')
        
    def main_loop(self):
        """
        This is where all of the big parts run
        """
        game = True
        while game:
            name,marker = self.players.player_turn()
            move = self.players.capture_player_move(name)
            x,y = self.get_x_y(move)
            # handle bad input
            if self.valid_move(x,y):
                self.set_square(x,y,marker)
                # way to recursive call until valid move 
            self.print_board()
            if self.check_win():
                    break
            if not len(self) > 0:
                game = False

    def valid_move(self,x,y):
        """
        Determines If a move is valid

        Arg:
            x: int the col index to check
            y: int the row index to check 
        """
        try:
            if not self.get_square(x,y):
                return True
            else:
                return False
        except:
            print("Invalid Move")
            return False

    def get_x_y(self,move):
        """
        Takes an int and converts it to x,y

        Arg:
            move: int player input

        Ret: 
            int,int x,y coordinates of move 
        """
        try:
            move = int(move)-1
            return (move%3),(move//3)
        except:
            return 

    def check_win(self):
        """
        Runs all win conditions and sees if there is a winner

        Ret:
            Bool
        """
        if self.check_rows():
            return True

        elif self.check_cols():
            return True

        return False

    def check_rows(self):
        """
        Checks all rows for 3 of a symbol in a row 
        
        Ret:
            Bool
        """
        for r in range(self.get_y_len()):
            row = self.get_row(r)
            if self.check_consec_values(row):
                return True
        return False

    def check_cols(self):
        """
        Checks all cols for 3 of a symbol in a col 
        
        Ret:
            Bool
        """
        for c in range(self.get_y_len()):
            col = self.get_col(c)
            if self.check_consec_values(col):
                return True
        return False

    def check_diag(self):
        """
        Checks all diagonals for 3 of a symbol in the diagonal
        
        Ret:
            Bool
        """
        pass

    def check_consec_values(self,lst):
        """
        This counts consecutive values in a list to determine 
            a winner

        Arg: 
            lst: list, input to count substrings 

        Ret: 
            bool, if 3 consecutive values 
        """
        cur_char = None
        char_count = 0
        for i in lst:
            if i == None:
                cur_char = i
                char_count = 0
            elif i != cur_char:
                cur_char = i
                char_count = 1
            else:
                char_count += 1
            if char_count == 3:
                return True
        return False


test = TicTacToe()
test.setup()
test.main_loop()