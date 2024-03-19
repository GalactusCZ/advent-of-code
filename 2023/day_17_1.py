def way(data: list[list[int]], pos: list[int], lengths: list[int], heat_loss: int):
    curr_data = data
    c_pos = pos
    depth = 3
    distance = (len(data) - pos[0]) + (len(data[0]) - pos[1])
    heat_loss += curr_data[c_pos[0]][c_pos[1]]

    curr_data[c_pos[0]][c_pos[1]] = 0

    # Check paths
    path_res = []

    # North
    if c_pos[0] - 1 >= 0 and curr_data[c_pos[0] - 1][c_pos[1]] != 0 and lengths[0] != 3:
        path_res.extend(path(curr_data, [c_pos[0] - 1, c_pos[1]], [lengths[0] + 1, 0, 0, 0], depth))
    # East
    if c_pos[1] + 1 < len(curr_data[0]) and curr_data[c_pos[0]][c_pos[1] + 1] != 0 and lengths[1] != 3:
        path_res.extend(path(curr_data, [c_pos[0], c_pos[1] + 1], [0, lengths[0] + 1, 0, 0], depth))
    # South
    if c_pos[0] + 1 < len(curr_data) and curr_data[c_pos[0] + 1][c_pos[1]] != 0 and lengths[2] != 3:
        path_res.extend(path(curr_data, [c_pos[0] + 1, c_pos[1]], [0, 0, lengths[0] + 1, 0], depth))
    # East
    if c_pos[1] - 1 >= 0 and curr_data[c_pos[0]][c_pos[1] - 1] != 0 and lengths[3] != 3:
        path_res.extend(path(curr_data, [c_pos[0], c_pos[1] - 1], [0, 0, 0, lengths[0] + 1], depth))

    path_scores = []
    for path in path_res:
        curr_res = 0
        for addr in path:
            curr_res += data[addr[0]][addr[1]]

        curr_res -= (((len(data) - path[0][0]) + (len(data[0]) - path[0][1])) - distance)

        path_scores.append(curr_res)

    minimal = path_res[path_scores.index(min(path_scores))]

    for mn in minimal:
        heat_loss += curr_data[mn[0]][mn[1]]
        curr_data[mn[0]][mn[1]] = 0

    heat_loss += way(curr_data, minimal[0], lengths)


def path(data: list[list[int]], pos: list[int], lengths: list[int], depth: int):
    curr_depth = depth - 1
    curr_data = data
    c_pos = pos
    path_res = []

    curr_data[pos[0]][pos[1]] = 0

    if curr_depth == 0:
        return [pos]

    else:
        # North
        if c_pos[0] - 1 >= 0 and curr_data[c_pos[0] - 1][c_pos[1]] != 0 and lengths[0] != 3:
            path_res.extend(path(curr_data, [c_pos[0] - 1, c_pos[1]], [lengths[0] + 1, 0, 0, 0], depth))
        # East
        if c_pos[1] + 1 < len(curr_data[0]) and curr_data[c_pos[0]][c_pos[1] + 1] != 0 and lengths[1] != 3:
            path_res.extend(path(curr_data, [c_pos[0], c_pos[1] + 1], [0, lengths[0] + 1, 0, 0], depth))
        # South
        if c_pos[0] + 1 < len(curr_data) and curr_data[c_pos[0] + 1][c_pos[1]] != 0 and lengths[2] != 3:
            path_res.extend(path(curr_data, [c_pos[0] + 1, c_pos[1]], [0, 0, lengths[0] + 1, 0], depth))
        # East
        if c_pos[1] - 1 >= 0 and curr_data[c_pos[0]][c_pos[1] - 1] != 0 and lengths[3] != 3:
            path_res.extend(path(curr_data, [c_pos[0], c_pos[1] - 1], [0, 0, 0, lengths[0] + 1], depth))

        new_path_res = []
        for res in path_res:
            new_path_res.append(res + [pos])

        return new_path_res

with open('day_17_test.txt') as f:
    data = f.read()
    data = data.split('\n')

    new_data = []
    for line in data:
        line = [int(x) for x in line]
        new_data.append(line)

    data = new_data

pos = [0,0]
lengths = [0,0,0,0]

result = way(data, pos, lengths, 0)

print(result)