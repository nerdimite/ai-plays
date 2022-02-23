from pyamaze import maze, agent


def solve_dfs(m):

    start = (m.rows, m.cols)

    explored = [start]
    frontier = [start]

    path = {}

    while len(frontier) > 0:

        curr_cell = frontier.pop()

        if curr_cell == (1, 1):
            break

        for d in 'ESNW':
            if m.maze_map[curr_cell][d]:
                if d == 'E':
                    child_cell = (curr_cell[0], curr_cell[1]+1)
                elif d == 'W':
                    child_cell = (curr_cell[0], curr_cell[1]-1)
                elif d == 'S':
                    child_cell = (curr_cell[0]+1, curr_cell[1])
                elif d == 'N':
                    child_cell = (curr_cell[0]-1, curr_cell[1])

                if child_cell in explored:
                    continue

                explored.append(child_cell)
                frontier.append(child_cell)

                path[child_cell] = curr_cell

    final_path = {}
    cell = (1, 1)
    while cell != start:
        final_path[path[cell]] = cell
        cell = path[cell]

    return final_path


def run():
    m = maze(7, 7)
    m.CreateMaze()

    path = solve_dfs(m)

    a = agent(m, footprints=True)
    m.tracePath({a: path})

    m.run()
