from pyamaze import maze, agent, COLOR


def solve_dfs(m):

    start = (m.rows, m.cols)

    explored = [start]
    frontier = [start]

    dfs_path = {}

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

                dfs_path[child_cell] = curr_cell

    final_path = {}
    cell = (1, 1)
    while cell != start:
        final_path[dfs_path[cell]] = cell
        cell = dfs_path[cell]

    return explored, dfs_path, final_path


def run(height=7, width=7, animate=False, delay=100):

    m = maze(height, width)
    m.CreateMaze(loopPercent=90)
    explored, dfs_path, final_path = solve_dfs(m)

    if animate:
        explorer = agent(m, footprints=True, color=COLOR.green, shape='square')
        reverse_agent = agent(m, 1, 1, footprints=True, color=COLOR.cyan,
                              shape='square', filled=True, goal=(m.rows, m.cols))
        final_agent = agent(m, footprints=True, color=COLOR.yellow,
                            shape='square', filled=False)

        m.tracePath({explorer: explored}, delay=delay)
        m.tracePath({reverse_agent: dfs_path}, delay=delay)
    else:
        final_agent = agent(m, footprints=True, color=COLOR.blue,
                            shape='square', filled=True)

    m.tracePath({final_agent: final_path}, delay=delay)

    m.run()
