# step 1: To display board
def display_board(board):
    print('\n' * 100)
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('--------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('--------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# board = []
board = ['#', 'X', 'O', 'X', 'X', 'X', 'O', 'X', 'O', 'X']
print(display_board(board))


# STEP 2: take player input X or O

def player_input():
    marker = ''

    while not (marker == 'X' or marker == 'O'):
        marker = input("Player 1, Please enter an input either X or O: ").upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# to define 2 different inputs to 2 players we do the following
player1_marker, player2_marker = player_input()
print(player_input())
print("Player 1: {}".format(player1_marker))  # player 1 o/p
print("Player 2: {}".format(player2_marker))  # player 2 o/p


# STEP  3: to define a board list object to a position
def place_marker(board, marker, position):
    board[position] = marker


# print(place_marker(board, 3, 'I'))
# print(display_board(board))


# STEP 4: to check if marker has won or not
def win_check(board, mark):
    return ((board[1] == board[2] == board[3] == mark) or
            (board[4] == board[5] == board[6] == mark) or
            (board[7] == board[8] == board[9] == mark) or
            (board[2] == board[5] == board[8] == mark) or
            (board[3] == board[6] == board[9] == mark) or
            (board[7] == board[4] == board[1] == mark) or
            (board[1] == board[5] == board[9] == mark) or
            (board[7] == board[5] == board[3] == mark))


# print(win_check('O', board))

# STEP 5: to randomly pick one player and choose who goes first

import random


def choose_first():
    choice = random.randint(0, 1)

    if choice == 0:
        return 'Player 1'
    else:
        return 'Player 2'


# print(choose_first())


# STEP 6: to check if the position on the board is available
def space_position(board, position):
    return board[position] == ' '


# print(space_position(board, 2))

# STEP 7: check if board is full using boolean
def board_check(board):
    for i in range(1, 10):
        if space_position(board, i):
            return False
    return True  # board is full we return True


# STEP 8: ask player to enter next position and use function from step 6 to see if that is a free position

def player_choice(board):
    position = 0

    while position not in range(1, 10) or not space_position(board, position):
        position = int(input('Choose position from (1-9): '))

    return position

# print(player_choice(board))
# print(player_choice(board))


# STEP 9: ask player if they want to play again
def replay():
    return input("Play again? Yes or No ").lower().startswith('y')

# print(replay())

# STEP 10: COMBINING WHOLE GAME

print("Welcome to Tic Tac Toe")

while True:
    # play the game

    ## set everything up(board, whose first, choose markers)
    the_board = [' '] * 10
    player1_marker, player2_marker = player_input()
    # print("Player 1: {}".format(player1_marker))  # player 1 o/p
    # print("Player 2: {}".format(player2_marker))  # player 2 o/p

    turn = choose_first()
    print(turn + ' will go first')

    play_game = input('Ready to play? y or n?')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    print(play_game)
    ### game play

    while game_on:
        if turn == 'Player 1':
            # show the board
            display_board(the_board)
            # choose a position
            position = player_choice(the_board)
            # place marker on the position
            place_marker(the_board, player1_marker, position)
            # check if they won or there is a tie
            if win_check(the_board, player1_marker):
                (display_board(the_board))
                print('Player 1 has won!!')
                game_on = False
            else:
                if board_check(the_board):
                    display_board(the_board)
                    print("TIE GAME!")
                    game_on = False
                else:
                    turn = 'Player 2'

    #### player two turn
    else:
        # show the board
        display_board(the_board)
        # choose a position
        position = player_choice(the_board)
        # place marker on the position
        place_marker(the_board, player2_marker, position)
        # print(place_marker())
        # check if they won or there is a tie
        if win_check(the_board, player2_marker):
            display_board(the_board)
            print('Player 2 has won!!')
            game_on = False
        else:
            if board_check(the_board):
                display_board(the_board)
                print("TIE GAME!")
                game_on = False
            else:
                turn = 'Player 1'

    if not replay():
        break
