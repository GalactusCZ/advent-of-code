Position = tuple[int, int]

    x, y = pos
    pos_dirs = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    curr_used = used.copy()
    curr_used.add(pos)

    for i, pos_dir in enumerate(pos_dirs):
        if pos_dir == end:
            return min(fastest_path, curr_path + 1 + 1000 * abs(i - direction))

        if pos_dir not in walls and pos_dir not in used:
            this_score = curr_path
            p_x, p_y = pos_dir

            if i == 0 or i == 2:
                while (p_x - 1, p_y) in walls and (p_x + 1, p_y) in walls:
                    this_score += 1

                    if i == 0 and (p_x, p_y - 1) not in walls:
                        p_y -= 1

                    elif i == 2 and (p_x, p_y + 1) not in walls:
                        p_y += 1

                    else:
                        break

            else:
                while (p_x, p_y - 1) in walls and (p_x, p_y + 1) in walls:
                    this_score += 1

                    if i == 1 and (p_x + 1, p_y) not in walls:
                        p_y += 1

                    elif i == 3 and (p_x - 1, p_y) not in walls:
                        p_y -= 1

                    else:
                        break

            retrieve = find_paths(pos_dir, end, walls, curr_used, curr_path + 1 + 1000 * abs(i - direction), fastest_path, i)
            fastest_path = min(fastest_path, retrieve)

    return fastest_path


with open("day_16.txt") as f:
    walls: set[tuple[int, int]] = set()

    for y, line in enumerate(f):
        for x, char in enumerate(line):
            if char == '#':
                walls.add((x, y))

            elif char == 'S':
                start = (x, y)

            elif char == 'E':
                end = (x, y)

fastest_path = 99999999999
lifo = []
