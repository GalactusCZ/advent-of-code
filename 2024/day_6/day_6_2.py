NORTH = 0
EAST = 1
SOUTH = 2
WEST = 3

def is_cycle(pos: tuple[int, int], direction: int, path_map: list[str], used: set[tuple[int,int]], trigger_streak: int) -> bool:
    new_x, new_y = pos

    for i in range(4):
        if i == direction:
            prev_x, prev_y = pos

            while (0 <= new_x < len(path_map[0])) and (0 <= new_y < len(path_map)) and path_map[new_y][new_x] != '#':
                if (new_x, new_y) in used:
                    trigger_streak += 1

                    if trigger_streak > 1000:
                        return True

                else:
                    trigger_streak = 0

                if path_map[new_y][new_x] != '#':
                    used.add((new_x, new_y))

                pos_continuations = [(new_x, new_y - 1), (new_x + 1, new_y), (new_x, new_y + 1), (new_x - 1, new_y)]

                prev_x = new_x
                prev_y = new_y
                new_x, new_y = pos_continuations[i]

            if not (0 <= new_x < len(path_map[0])) or not (0 <= new_y < len(path_map)):
                return False

            if path_map[new_y][new_x] == '#':
                direction = (direction + 1) % 4
                new_x = prev_x
                new_y = prev_y

            return is_cycle((new_x, new_y), direction, path_map, used, trigger_streak)

def count_path(pos: tuple[int, int], direction: int, path_map: list[str]) -> int:
    x, y = pos
    pos_paths = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    adder = 1
    if path_map[y][x] == "X":
        adder = 0

    for i in range(4):
        if i == direction:
            new_x, new_y = pos_paths[i]

            path_map[y] = path_map[y][:x] + 'X' + path_map[y][x + 1:]
            count = adder
            prev_x, prev_y = pos

            while (0 <= new_x < len(path_map[0])) and (0 <= new_y < len(path_map)) and path_map[new_y][new_x] != '#':
                pos_continuations = [(new_x, new_y - 1), (new_x + 1, new_y), (new_x, new_y + 1), (new_x - 1, new_y)]

                if path_map[new_y][new_x] != 'X':
                    count += 1
                    path_map[new_y] = path_map[new_y][:new_x] + 'X' + path_map[new_y][new_x + 1:]

                prev_x = new_x
                prev_y = new_y
                new_x, new_y = pos_continuations[i]

            if not (0 <= new_x < len(path_map[0])) or not (0 <= new_y < len(path_map)):
                return count

            if path_map[new_y][new_x] == '#':
                direction = (direction + 1) % 4
                new_x = prev_x
                new_y = prev_y

            return count + count_path((new_x, new_y), direction, path_map)

with open("day_6.txt") as f:
    path_map: list[str] = []

    for y, line in enumerate(f):
        line = line.replace('\n', '')

        if '^' in line:
            guard_pos = (line.index('^'), y)

        path_map.append(line)

    filler_map = path_map.copy()
    count_path(guard_pos, NORTH, filler_map)

    count = 0
    for y, line in enumerate(filler_map):
        for x, char in enumerate(line):
            if (x, y) != guard_pos and filler_map[y][x] == 'X':
                new_map = path_map.copy()
                new_map[y] = new_map[y][:x] + '#' + new_map[y][x + 1:]

                if is_cycle(guard_pos, NORTH, new_map, set(), 0):
                    count += 1

    print(count)
