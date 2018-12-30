# design the board
# ask player to select a marker

# def display_board(board):
#     print(board[1] + '|' + board[2] + '|' + board[3])
#     print(board[1] + '|' + board[2] + '|' + board[3])
#     print(board[1] + '|' + board[2] + '|' + board[3])
#
#
# test_board = ['#', 'X', 'O', 'X', 'O', 'X', 'O', 'X', 'O', 'X']
# display_board(test_board)


def display_board(board):
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[1] + '|' + board[2] + '|' + board[3])
    print(board[1] + '|' + board[2] + '|' + board[3])


test_board = [' '] * 10
display_board(test_board)



def player_input():

    '''
    :return: (Player 1 marker, Player 2 marker)
    '''

    marker = ''
    while marker != 'X' and marker != 'O':
    # while not(marker == 'X' and marker == 'O'):    can use this stmt as well
        marker = input("Player 1: Select X or O: ").upper()
    if marker == 'X':
        return('X','O')
    else:
        return('O','X')
print(player_input())








