import argparse
import numpy as np
from time import sleep
from terminal_utils import write, move


def validate(board):
    '''
    Takes a board array as input and checks if the queens placed currently
    are valid or not. It does NOT check if a solution is reached.
    '''
    n = board.shape[0]

    # Check if each row and column has only 1 queen
    for row in range(n):
        if board[row].sum() > 1:
            return False

    for col in range(n):
        if board[col].sum() > 1:
            return False

    # Check all diagonals
    diagonals = ([board.diagonal(i) for i in range(-n+1, n)] +
                 [board[::-1, :].diagonal(i) for i in range(-n+1, n)])

    for d in diagonals:
        if len(d) > 1:
            if d.sum() > 1:
                return False

    return True


def csp_solver(board, col, is_animate=False):
    '''Solves the NQueens problem (CSP) using Backtracking'''
    n = board.shape[0]

    if validate(board):
        if board.sum() == n:
            return True

        for row in range(n):
            board[row, col] = 1

            if is_animate:
                visualize(n, row, col, '👑')
                sleep(0.05)

            if validate(board):
                if csp_solver(board, col+1, is_animate):
                    return True
                else:
                    board[row, col] = 0

                    if is_animate:
                        visualize(n, row, col, viz_board[row][col])
                        sleep(0.05)
            else:
                board[row, col] = 0

                if is_animate:
                    visualize(n, row, col, viz_board[row][col])
                    sleep(0.05)
    else:
        return False


def visualize(n, row, col, to_place='👑'):
    '''
    Visualizes the board in the terminal and places the 
    queen at a particular location on the board
    '''
    move(n - row + 1, 'up')
    if col > 0:
        move(col * 2, 'right')
        write(f"{to_place}")
    else:
        write(to_place)
    write("\n" * (n - row + 1))


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Solves the NQueens Problem using Backtracking')
    parser.add_argument('-n', '--nqueens', type=int,
                        default=6, help="Number of queens. Default is 6.")
    parser.add_argument('--animate', action='store_true',
                        help='Use this flag to animate the backtracking process as it explores and places the queens on the board.')
    args = parser.parse_args()

    # Define problem
    n = args.nqueens
    if n < 4:
        print('⚠️ Minimum number of queens must be 4')
        exit()
    board = np.zeros((n, n))

    print(f'⚙️Backtracking to solve {n}-Queens...')

    # ======== Visualize Board ========
    # black and white boxes
    squares = ['🔲', '🔳']
    s = 0
    # a copy of board with colors for reference during animation
    viz_board = board.tolist()

    print()
    for i in range(n):
        if s:
            s = 0
        else:
            s = 1
        for j in range(n):
            print(squares[s], end='')
            viz_board[i][j] = squares[s]
            if s:
                s = 0
            else:
                s = 1
        print()
    print()

    # ======== Solve the CSP Problem ========
    if csp_solver(board, 0, args.animate):
        is_solved = True
    else:
        is_solved = False

    # ======== Print the Solution on the Board ========
    for row in range(n):
        for col in range(n):
            if board[row, col] == 1:
                visualize(n, row, col)

    if is_solved:
        print('✅ Problem Solved Successfully 🎉')
    else:
        print('❌ Failed to Solve')
