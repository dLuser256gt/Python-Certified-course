"""
Tic Tac Toe game with console play
"""

import random


# 1 Board setup

def display_board(board):
    print("\n" * 100)  # Reset the board everytime so that the console is clean

    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')


# 2 Take inputs from player -> Can be X or O

def player_input():  # Will return a tuple with the first element being the player choice and the second the computer
    marker = ''
    while marker not in ['X', 'O']:
        marker = input('Pick your poison, X or O?: ').upper()

    if marker == 'X':
        return 'X', 'O'
    else:
        return 'O', 'X'


# 3 Place the marker on a position of the board

def place_marker(board, marker, position):
    board[position] = marker


# 4 Check to see if someone won the game

def win_check(board, mark):
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or  # across the top
            (board[4] == mark and board[5] == mark and board[6] == mark) or  # across the middle
            (board[1] == mark and board[2] == mark and board[3] == mark) or  # across the bottom
            (board[7] == mark and board[4] == mark and board[1] == mark) or  # down the middle
            (board[8] == mark and board[5] == mark and board[2] == mark) or  # down the middle
            (board[9] == mark and board[6] == mark and board[3] == mark) or  # down the right side
            (board[7] == mark and board[5] == mark and board[3] == mark) or  # diagonal
            (board[9] == mark and board[5] == mark and board[1] == mark))  # diagonal


# 5 Randomly select the first player

def choose_first():
    if random.randint(0, 1) == 0:
        return 'Player 2'
    else:
        return 'Player 1'


# 6 Verify if a space on the board is empty

def space_check(board, position):
    return board[position] == ' '


# 7 Verify if the board is full

def full_board_check(board):
    for i in range(1, 10):
        if space_check(board, i):
            return False
    return True


# 8 Ask the player to select a position on the board to put his mark and verify if the position is empty

def player_choice(board):
    position = 0

    while position not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))

    return position


# 9 Ask for a replay

def replay():
    return input('Do you want to play again? Enter Yes or No: ').lower().startswith('y')


# 10 Game logic

print('Welcome to my Tic Tac Toe game, hope you placed your bets!')

while True:
    game_board = [' '] * 10  # Empty board
    player1_marker, player2_marker = player_input()  # Assigning the player markers
    turn = choose_first()  # Random chose the first player
    print(turn + ' will go first.')

    play_game = input('Are you ready to play? Enter Yes or No.')

    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'Player 1':
            # Player1's turn.

            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player1_marker, position)

            if win_check(game_board, player1_marker):
                display_board(game_board)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 2'

        else:
            # Player2's turn.

            display_board(game_board)
            position = player_choice(game_board)
            place_marker(game_board, player2_marker, position)

            if win_check(game_board, player2_marker):
                display_board(game_board)
                print('Player 2 has won!')
                game_on = False
            else:
                if full_board_check(game_board):
                    display_board(game_board)
                    print('The game is a draw!')
                    break
                else:
                    turn = 'Player 1'

    if not replay():
        break
