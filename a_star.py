from math import inf

MAZE = [
    [True, True, True, True, False, True, True, True],
    [True, True, False, False, False, True, True, True],
    [True, True, True, True, False, True, True, True],
    [True, True, True, True, False, True, True, True],
    [True, True, True, True, False, True, True, False],
    [True, True, True, True, False, True, True, True],
    [True, True, False, False, False, False, False, True],
    [True, True, True, True, True, True, True, True],
]


def print_maze(path, start, finish):
    for y in range(len(MAZE)):
        for x in range(len(MAZE[y])):
            if (x, y) == start:
                print("1", end="")
            elif (x, y) == finish:
                print("2", end="")
            elif (x, y) in path:
                print("O", end="")
            elif MAZE[y][x] is True:
                print(" ", end="")
            else:
                print("X", end="")
        print()


def add(t1, t2):
    return t1[0] + t2[0], t1[1] + t2[1]


def h(path, finish):
    """ manhattan distance """
    return len(path) + abs(path[-1][0] - finish[0]) + abs(path[-1][1] - finish[1])


def out_of_map(p):
    if 0 <= p[1] < len(MAZE) and 0 <= p[0] < len(MAZE[0]):
        return False
    return True


def a_star(current, finish):
    path = [current]
    hs = {current: h(path, finish)}
    ps = {current: path.copy()}
    expl = {current: True}

    while path[-1] != finish:
        # generate neighbors
        for move in [(1, 0), (-1, 0), (0, 1), (0, -1)]:
            pos = add(path[-1], move)

            # is obstacle or edge
            if out_of_map(pos) or MAZE[pos[1]][pos[0]] is False:
                continue

            # evaluate new path
            new_path = path.copy()
            new_path.append(pos)
            ph = h(new_path, finish)

            # new best?
            if new_path[-1] not in hs or ph < hs[new_path[-1]]:
                hs[new_path[-1]] = ph
                ps[new_path[-1]] = new_path
                expl[new_path[-1]] = False

        # find closest unexplored
        dist = inf
        unexplored_keys = [key for key in expl.keys() if expl[key] is False]
        for u_key in unexplored_keys:
            if hs[u_key] < dist:
                closest = u_key
                dist = hs[closest]

        # no unexplored
        if dist == inf:
            print("Path not found")
            return

        # prepare next iteration
        path = ps[closest]
        expl[closest] = True

    print("Found")
    return path


start = (1, 4)
finish = (7, 3)
print_maze([], start, finish)
solution = a_star(start, finish)
print(solution)
print_maze(solution, start, finish)
