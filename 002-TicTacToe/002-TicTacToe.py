# 002-TicTacToe.py
# A simple CLI tic-tac-toe program
# New concepts: array, string formatting, for loops

board = [' '] * 9
currentTurn = 0      # 0 = X, 1 = O
ended = False

while not ended:
    # Write board
    print('Top left is 1; Top right is 3; Bottom right is 9')
    print()
    print('{0}|{1}|{2}'.format(board[0],board[1],board[2]))
    print('-+-+-')
    print('{0}|{1}|{2}'.format(board[3],board[4],board[5]))
    print('-+-+-')
    print('{0}|{1}|{2}'.format(board[6],board[7],board[8]))

    # Prompt input
    isMoveValid = False

    while True:
        if currentTurn == 0:
            thisMove = input('X, please input the grid number (1-9): ')
        else:
            thisMove = input('O, please input the grid number (1-9): ')
        thisMove = int(float(thisMove))

        if (thisMove in range(1,10)) and (board[thisMove-1] == ' '):
            break
        else:
            print('Invalid move, try again')

    # Apply move to board
    board[thisMove-1] = 'X' if currentTurn == 0 else 'O'    

    # Check game over
    # Check column
    for i in range(2):
        if board[i] == board[i+3] == board[i+6] != ' ':
            ended = True
            winner = board[i]
    # Check row
    for i in range(0,7,3):
        if board[i] == board[i+1] == board[i+2] != ' ':
            ended = True
            winner = board[i]

    # Check diagonals
    if board[0] == board[4] == board[8] != ' ':
        ended = True
        winner = board[0]
    elif board[2] == board[4] == board[6] != ' ':
        ended = True
        winner = board[2]

    # Check board full
    if (not ended) and (' ' not in board):
        ended = True
        winner = 'Tie'

    # Swap currentTurn
    currentTurn = 1 - currentTurn

# End of game message
print()
print()
print('{0}|{1}|{2}'.format(board[0],board[1],board[2]))
print('-+-+-')
print('{0}|{1}|{2}'.format(board[3],board[4],board[5]))
print('-+-+-')
print('{0}|{1}|{2}'.format(board[6],board[7],board[8]))
print()
if winner == 'Tie':
    print('Tie!')
else:
    print(winner + ' won!')
