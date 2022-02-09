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
                        visualize(n, row, col, ' ')
                        sleep(0.05)
            else:
                board[row, col] = 0

                if is_animate:
                    visualize(n, row, col, ' ')
                    sleep(0.05)
    else:
        return False


def visualize(n, row, col, to_place='👑'):
    '''
    Visualizes the board in the terminal and places the 
    queen at a particular location on the board
    '''
    # move((n * 2) - (row * 2) + 2, 'up')
    # if col > 0:
    #     move((col * 5), 'right')
    # write(f" {to_place} ")
    # write("\n" * ((n * 2) - (row * 2) + 2))

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
    parser.add_argument('--viz_array', action='store_true')
    args = parser.parse_args()

    n = args.nqueens

    print(f'⚙️Backtracking to solve {n}-Queens...')
    # Print Chess Board
    print()
    squares = ['🔲', '🔳']
    s = 0
    for i in range(n):
        if s:
            s = 0
        else:
            s = 1
        for j in range(n):
            print(squares[s], end='')
            if s:
                s = 0
            else:
                s = 1
        print()
    print()

    # for i in range(n):
    #     print("    |" * (n-1) + "    ")
    #     if i < n-1:
    #         print("—————" * (n-1) + "————")
    # print()

    # Solve the CSP Problem
    board = np.zeros((n, n))

    if csp_solver(board, 0, args.animate):
        is_solved = True
    else:
        is_solved = False

    # Print the Solution on the Board
    for row in range(n):
        for col in range(n):
            if board[row, col] == 1:
                visualize(n, row, col)

    # # Print array in case of
    # if n > 8:
    #     print('Printing a smaller array version of the solution board as the visualization would \
    #         have gotten messed up at large numbers due to scrolling.')
    #     board_list = board.tolist()
    #     for row in range(n):
    #         for col in range(n):
    #             if board[row, col] == 1:
    #                 board_list[row][col] = '👑'
    #             else:
    #                 board_list[row][col] = '🟦'
    #     print(np.array(board_list))

    if is_solved:
        print('✅ Problem Solved Successfully 🎉')
    else:
        print('❌ Failed to Solved')
