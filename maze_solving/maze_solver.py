import argparse
from dfs import run as dfs
from bfs import run as bfs

if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Solves a Maze using Various Search Algorithms')
    parser.add_argument('--algo', type=str, default='dfs',
                        choices=['dfs', 'bfs'], help="Search Algorithm to use to solve the Maze. Default is bfs.")
    parser.add_argument('--height', type=int, default=10,
                        help="Height of Maze in number of cells. Default is 10.")
    parser.add_argument('--width', type=int, default=20,
                        help="Width of Maze in number of cells. Default is 20.")
    parser.add_argument('--animate', action='store_true',
                        help='Use this flag to fully animate the search process as the agent explores the maze.')
    parser.add_argument('--delay', type=int, default=100,
                        help="Delay between each animation step in milliseconds. Default is 150ms.")
    args = parser.parse_args()

    if args.algo == 'dfs':
        dfs(args.height, args.width, args.animate, args.delay)

    if args.algo == 'bfs':
        bfs(args.height, args.width, args.animate, args.delay)
