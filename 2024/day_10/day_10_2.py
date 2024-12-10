def path_finder(plain_map: list[list[int]], pos: tuple[int, int],
                searched: set[tuple[int, int]],
                cache: dict[tuple[int, int], int]) \
                -> int:
    paths_found = 0
    x, y = pos
    curr_val = plain_map[y][x]
    pos_dirs = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]

    for dir in pos_dirs:
        p_x, p_y = dir

        if 0 <= p_x < len(plain_map[0]) and 0 <= p_y < len(plain_map) and \
           plain_map[p_y][p_x] == curr_val + 1:
            if plain_map[p_y][p_x] == 9:
                paths_found += 1

            elif dir in searched:
                paths_found += cache[dir]

            else:
                searched.add(pos)
                cache[pos] = 0
                paths_found += path_finder(plain_map, dir, searched, cache)

    searched.add(pos)
    cache[pos] = paths_found

    return paths_found


with open("day_10.txt") as f:
    starts: set[tuple[int, int]] = set()
    plain_map: list[list[int]] = []

    for y, line in enumerate(f):
        line = line.replace('\n', '')
        new_line: list[int] = []

        for x, char in enumerate(line):
            new_line.append(int(char))

            if char == '0':
                starts.add((x, y))

        plain_map.append(new_line)

    cache: dict[tuple[int, int], int] = {}
    searched: set[tuple[int, int]] = set()
    result = 0

    for start in starts:
        test = path_finder(plain_map, start, searched, cache)
        print(test)
        result += test

    print(result)

