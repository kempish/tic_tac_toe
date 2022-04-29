from msvcrt import getwch
import random

# (GLOBAL) VARIABLES

# PLAYER SIGN - we got player X and O and we start with X player
player = 'X'

# CONTINUE GAME - variable for end game if someone win or in case of tie
game_is_on = True

# PLAY WIH COMPUTER
# choose player vs player mode or play with computer
print('\nplay with computer [C]\nplay with other player [P]')
player_or_computer = getwch()

# user can only choose between C and P
while player_or_computer.capitalize() not in ['C', 'P']:
    print('\nplease enter \'C\' or \'P\'\nplay with computer [C]\nplay with other player [P]')
    player_or_computer = getwch()

# user wants to play with computer → True otherwise → False
play_with_computer = True if player_or_computer.capitalize() == 'C' else False

# KEYBORD MODE - choose standard or numeric
print('\nStandard\n1|2|3\n4|5|6\n7|8|9\n\nor\n\nNumeric\n7|8|9\n4|5|6\n1|2|3\n\nchoose keyboard mode [S/N]')
choose_keyboard = getwch()

# limit user answer to S and N
while choose_keyboard.capitalize() not in ['S', 'N']:
    print('\nplease enter \'S\' for standard keyboard mode or \'N\' for numeric keyboard mode')
    choose_keyboard = getwch()

numeric_keyboard = True if choose_keyboard.capitalize() == 'N' else False


class Board():    

    def __init__(self, board) -> None:
        self.board = board
        # necessary to break function when computer makes move (in AI mode)
        self.computer_turn = False


    # display board 3x3
    def __repr__(self) -> str:
        return (f'\n{self.board[0]} | {self.board[1]} | {self.board[2]}\n'
                f'{self.board[3]} | {self.board[4]} | {self.board[5]}\n'
                f'{self.board[6]} | {self.board[7]} | {self.board[8]}\n')


    # here players will choose which field they want to mark
    def choose_field(self, player):

        # whose turn now? [prompt depends on play mode]
        if play_with_computer:
            print('it\'s your turn')
        else:
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


    # after each turn - change player automatically (also when we play with AI)
    def change_player(self):
        global player
        global play_with_computer
        
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
    

    # function for simplification AI_mode function - mark empty field to defeat or block player - in case like this: block || X | block | X || or defeat || O | O | defeat || etc. [computer plays as O player]
    def find_best_field(self, range, field_index_in_range, player, function):
        # computer can use this function for either defeat or block player - func parameter determine what is this function use for
        sign = 'X' if function == 'block' else 'O'
        
        # is still computers turn?
        if self.computer_turn:
            # check if two same signs
            if range.count(sign) == 2 and range.count('-') == 1:
                # if two same signs and one empty field - fill empty with computer's sign
                for field_index in field_index_in_range:
                    if self.board[field_index] == '-':
                        self.board[field_index] = player
                        self.computer_turn = False
        else:
            pass
    
    
    # AI mode - if computer has no opportunity to neither defeat nor block player - let it fill random empty field
    def fill_random(self):
        empty_fields = []
        for index, field in enumerate(self.board):
            if field == '-':
                empty_fields.append(index)
        
        # try to fill random field | if no more empty fields → it's a tie
        try:
            self.board[random.choice(empty_fields)] = player
        except:
            return self.tie()


    # in case user chose playing with computer → AI mode
    def AI_mode(self, player):

        print('computer\'s turn:')
        
        # rows
        row_one = [self.board[0], self.board[1], self.board[2]]
        row_two = [self.board[3], self.board[4], self.board[5]]
        row_three = [self.board[6], self.board[7], self.board[8]]
        # columns
        column_one = [self.board[0], self.board[3], self.board[6]]
        column_two = [self.board[1], self.board[4], self.board[7]]        
        column_three = [self.board[2], self.board[5], self.board[8]]
        # diagonals
        diagonal_one = [self.board[0], self.board[4], self.board[8]]
        diagonal_two = [self.board[2], self.board[4], self.board[6]]

        # list of arguments required to execute find_best_field() function
        steps = [
            # try to defeat/block rival in rows eg. X | - | X → X | O | X
            [row_one, [0, 1, 2]],
            [row_two, [3, 4, 5]],
            [row_three, [6, 7, 8]],

            # as above but try to defeat/block in columns
            [column_one, [0, 3, 6]],
            [column_two, [1, 4, 7]],
            [column_three, [2, 5, 8]],

            # as above but try to defeat/block in diagonals
            [diagonal_one, [0, 4, 8]],
            [diagonal_two, [2, 4, 6]],
        ]

        # call defeat player function with above arguments (computer tries to find possibility to defeat player)
        for step in steps:
            self.find_best_field(step[0], step[1], player, 'defeat')

        # if not defeated → call block player function with above arguments (computer tries to find possibility to block player)
        for step in steps:
            self.find_best_field(step[0], step[1], player, 'block')

        # no opportunities to defeat/block player? → choose random field
        if self.computer_turn:
            self.fill_random()


board = Board(['-', '-', '-', 
               '-', '-', '-',
               '-', '-', '-'])


while game_is_on:
    print(board)
    if play_with_computer and player == 'O':
        board.computer_turn = True
        board.AI_mode(player)
    else:
        board.choose_field(player)
    board.check_row()
    board.check_column()
    board.check_diagonal()
    board.tie()
    board.change_player()

