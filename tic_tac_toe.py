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


# display board
def display_board():
    print(f'\n{board[0]} | {board[1]} | {board[2]}\n'
          f'{board[3]} | {board[4]} | {board[5]}\n'
          f'{board[6]} | {board[7]} | {board[8]}')


# decide where to put your mark
def choose_field(player):
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
        if board[int(answer) - 1] != '-':
            print('This field is already taken! Choose another one.')
        else:
            ask_again = False

    # mark field with player's mark
    board[int(answer) - 1] = player


# after each turn - change player automatically
def change_player():
    global player

    # it was player's X turn → change to player O
    if player == 'X':
        player = 'O'
    # it was player's O turn → change to player X
    elif player == 'O':
        player = 'X'


# check in rows if somebody won
def check_row():
    global game_is_on

    row_one = board[0] == board[1] == board[2] != '-'
    row_two = board[3] == board[4] == board[5] != '-'
    row_three = board[6] == board[7] == board[8] != '-'

    # one of rows contains three same mark → end game, player X/O won
    if row_one or row_two or row_three:
        game_is_on = False
        display_board()
        print(f'\n{player} won')


# check in columns if somebody won
def check_column():
    global game_is_on

    column_one = board[0] == board[3] == board[6] != '-'
    column_two = board[1] == board[4] == board[7] != '-'
    column_three = board[2] == board[5] == board[8] != '-'

    # one of columns contains three same mark → end game, player X/O won
    if column_one or column_two or column_three:
        game_is_on = False
        display_board()
        print(f'\n{player} won')


# check in diagonal if somebody won
def check_diagonal():
    global game_is_on

    diagonal_one = board[0] == board[4] == board[8] != '-'
    diagonal_two = board[2] == board[4] == board[6] != '-'

    # one of diagonals contains three same mark → end game, player X/O won
    if diagonal_one or diagonal_two:
        game_is_on = False
        display_board()
        print(f'\n{player} won')


# end game if tie
def tie():
    global game_is_on

    # count every empty field on board
    empty_count = 0
    for x in board:
        if x == '-':
            empty_count += 1
    
    # if no empty field → end the game
    if empty_count == 0:
        display_board()
        print('\nGame over! It\'s a tie!\n')
        game_is_on = False


# in case user chose playing with computer
def AI_mode():
    pass


# run a game
while game_is_on:
    display_board()
    choose_field(player)
    check_row()
    check_column()
    check_diagonal()
    change_player() if not play_with_computer else AI_mode()
    tie()
