from msvcrt import getwch

# global values
board = ['-', '-', '-', 
         '-', '-', '-',
         '-', '-', '-']

# we got player X and O and we start with X player
player = 'X'

# opportunity to end game if someone win or in case of tie
game_is_on = True

# choose player vs player or play with computer
play_with_computer = False
print('\nplay with computer [C]\nplay with other player [P]')
player_or_computer = getwch()

# user can only choose between C and P
while player_or_computer.capitalize() not in ['C', 'P']:
    print('\nplease enter \'C\' or \'P\'\nplay with computer [C]\nplay with other player [P]')
    player_or_computer = getwch()

# user wants to play with computer → True otherwise → False
play_with_computer = True if player_or_computer.capitalize() == 'C' else False

class Board():
    def __init__(self, board) -> None:
        self.board = board

    # display board 3x3
    def __repr__(self) -> str:
        return (f'\n{self.board[0]} | {self.board[1]} | {self.board[2]}\n'
                f'{self.board[3]} | {self.board[4]} | {self.board[5]}\n'
                f'{self.board[6]} | {self.board[7]} | {self.board[8]}\n')


    # here players will choose which field they want to mark
    def choose_field(self, player):
        global board

        # whose turn now?
        print(f'\nit\'s {player}\'s turn')

        # loop until answer will be in range 1-9 and will point unmarked field
        ask_again = True
        while ask_again:
            answer = input('which field do you choose? (1-9): ')

            # check if answer is in range 1-9
            while answer not in ['1', '2', '3', '4', '5', '6', '7', '8', '9']:
                answer = input('which field do you choose? (1-9): ')

            # check if choosen field is already taken
            if self.board[int(answer) - 1] != '-':
                print('This field is already taken! Choose another one.')
            else:
                ask_again = False

        # mark field with player's mark
        self.board[int(answer) - 1] = player


    # after each turn - change player automatically (unless we play with AI)
    def change_player(self):
        global player

        # it was player's X turn → change to player O
        if player == 'X':
            player = 'O'
        # it was player's O turn → change to player X
        elif player == 'O':
            player = 'X'


    # check in rows if somebody won
    def check_row(self):
        global game_is_on

        # one of rows contains three same mark → end game, player X/O won | row 1 or row 2 or row 3 |
        if self.board[0] == self.board[1] == self.board[2] != '-' or self.board[3] == self.board[4] == self.board[5] != '-' or self.board[6] == self.board[7] == self.board[8] != '-':
            game_is_on = False
            print(board)
            print(f'\n{player} won')


    # check in columns if somebody won
    def check_column(self):
        global game_is_on

        # one of columns contains three same mark → end game, player X/O won | column 1 or column 2 or column 3 |
        if self.board[0] == self.board[3] == self.board[6] != '-' or self.board[1] == self.board[4] == self.board[7] != '-' or self.board[2] == self.board[5] == self.board[8] != '-':
            game_is_on = False
            print(board)
            print(f'\n{player} won')
    

    # check in diagonal if somebody won
    def check_diagonal(self):
        global game_is_on

        # one of diagonals contains three same mark → end game, player X/O won | diagonal 1 or diagonal 2 |
        if self.board[0] == self.board[4] == self.board[8] != '-' or self.board[2] == self.board[4] == self.board[6] != '-':
            game_is_on = False
            print(board)
            print(f'\n{player} won')


    # end game if tie
    def tie(self):
        global game_is_on

        # count every empty field on board
        empty_count = 0
        for x in self.board:
            if x == '-':
                empty_count += 1
        
        # if no empty field → end the game
        if empty_count == 0:
            print(board)
            print('\nGame over! It\'s a tie!\n')
            game_is_on = False
    
    
    # in case user chose playing with computer
    def AI_mode():
        pass


board = Board(['-', '-', '-', 
               '-', '-', '-',
               '-', '-', '-'])


while game_is_on:
    print(board)
    board.choose_field(player)
    board.check_row()
    board.check_column()
    board.check_diagonal()
    board.tie()
    board.change_player()

