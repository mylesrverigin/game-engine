class Player:
    def __init__(self,name,marker):
        """
        Makes a player object 
        
        Arg:
            name: str name of player
            marker: str marker of player pieces
        """
        self.name = name
        self.marker = marker

    def ret_name(self):
        """
        Returns Player Name
        """
        return self.name

    def ret_marker(self):
        """
        Returns Player Marker
        """
        return self.marker

class PlayerQue:
    def __init__(self):
        self.players = []
        self.num_players = 0
        self.current_turn = 0

    def add_players(self):
        """
        Adds players based on User input
            creates Player class instance for each
            players stored in self.players list
        Stores number of players in game
        """
        print("How many Players?")
        players = input()
        for i in range(self.input_to_int(players)):
            print('Enter P{} Name'.format(i+1))
            name = input()
            print('Enter P{} Marker'.format(i+1))
            marker = input()
            self.players.append(Player(name,marker))
        self.num_players = len(self.players)
        print("Players Added")
        

    def input_to_int(self,value):
        """
        Takes user input and turns it into an int
        
        Returns
            value or makes user try again
        """
        try: 
            return int(value)
        except:
            print("Invalid Input Try again")
            value = input()
            return self.input_to_int(value)

    def make_turn_order(self):
        """
        Scrambles the self.players order for who starts
        """
        self.players = list(set(self.players))

    def player_turn(self):
        """
        Takes a Player from self.players 

        Returns
            Player name 
            Player Marker 
            Increments current_turn
        """
        current_player = self.players[self.current_turn]
        self.current_turn += 1
        if self.current_turn == self.num_players:
            self.current_turn = 0
        return current_player.ret_name(), current_player.ret_marker()
        
    def ret_num_players(self):
        return self.num_players

    def add_player(self):
        """
        Adds a Single Player to game
        """
        pass

    def capture_player_move(self,name):
        print("{} Enter Move".format(name))
        move = input()
        return move