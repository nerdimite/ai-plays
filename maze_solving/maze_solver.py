import argparse
from dfs import run as dfs

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Solves the NQueens Problem using Backtracking')
    parser.add_argument('-a', '--algo', type=str, default='dfs',
                        choices=['dfs', 'bfs'], help="Search Algorithm to use to solve the Maze. Default is bfs.")
    args = parser.parse_args()

    if args.algo == 'dfs':
        dfs()
