# Solve a Maze using Search Algorithms

This is an implementation of various search algorithms for solving a maze like DFS, BFS, A\*, etc.

## Prerequisites

Before you run any of the codes, install `pyamaze` by running `pip install pyamaze`.

## Usage

You can run the maze solving program using different algorithms as shown below:

### Depth-first Search

This algorithm is faster but doesn't guarantee the shortest path.

```
python maze_solver.py --algo dfs
```

With Full Animation,

```
python maze_solver.py --algo dfs --animate
```

### Breadth-first Search

This algorithm is slower but guarantees the shortest path.

```
python maze_solver.py --algo bfs
```

With Full Animation,

```
python maze_solver.py --algo bfs --animate
```

## Arguments Reference

```bash
usage: maze_solver.py [-h] [--algo {dfs,bfs}] [--height HEIGHT] [--width WIDTH] [--animate] [--delay DELAY]

Solves a Maze using Various Search Algorithms

optional arguments:
  -h, --help        show this help message and exit
  --algo {dfs,bfs}  Search Algorithm to use to solve the Maze. Default is bfs.
  --height HEIGHT   Height of Maze in number of cells. Default is 7.
  --width WIDTH     Width of Maze in number of cells. Default is 7.
  --animate         Use this flag to fully animate the search process as the agent explores the maze.
  --delay DELAY     Delay between each animation step in milliseconds. Default is 150ms.
```

## References

- [Depth First Search (DFS) in Python](https://youtu.be/sTRK9mQgYuc)
- [Breadth First Search (BFS) in Python](https://youtu.be/D14YK-0MtcQ)
