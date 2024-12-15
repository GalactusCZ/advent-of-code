def move(walls: set[tuple[int, int]], boxes: set[tuple[int, int, int]], moves: str, pos: tuple[int, int], height: int, width: int) -> tuple[set[tuple[int, int, int]], tuple[int, int]]:
    for mov in moves:
        x, y = pos

        if mov == '^':
            next_pos = (x, y - 1)
            direction = 0

        elif mov == '>':
            next_pos = (x + 1, y)
            direction = 1

        elif mov == 'v':
            next_pos = (x, y + 1)
            direction = 2

        else:
            next_pos = (x - 1, y)
            direction = 3

        if next_pos in [(x, y) for x, y, _ in boxes]:
            pre_change = boxes.copy()

            if move_boxes(walls, boxes, direction, next_pos):
                pos = next_pos

            else:
                boxes = pre_change

        elif next_pos not in walls:
            pos = next_pos

        # print(mov)
        # for y in range(height):
        #     line = ''
        #     for x in range(width * 2):
        #         if (x, y) in walls:
        #             line += '#'

        #         elif (x, y, 0) in boxes:
        #             line += '['

        #         elif (x, y, 1) in boxes:
        #             line += ']'

        #         elif (x, y) == pos:
        #             line += '@'

        #         else:
        #             line += '.'

        #     print(line)

    return (boxes, pos)


def move_boxes(walls: set[tuple[int, int]], boxes: set[tuple[int, int, int]], direction: int, pos: tuple[int, int]) -> bool:
    x, y = pos
    connections = {(x, y): con for x, y, con in boxes}

    if direction == 0:
        if connections[pos] == 0:
            pos_dirs = [(x, y - 1), (x + 1, y - 1)]
        else:
            pos_dirs = [(x - 1, y - 1), (x, y - 1)]

    elif direction == 1:
        pos_dirs = [(x + 2, y)]

    elif direction == 2:
        if connections[pos] == 0:
            pos_dirs = [(x, y + 1), (x + 1, y + 1)]
        else:
            pos_dirs = [(x - 1, y + 1), (x, y + 1)]

    else:
        pos_dirs = [(x - 2, y)]

    for pos_dir in pos_dirs:
        if pos_dir in walls:
            return False

    for i, pos_dir in enumerate(pos_dirs):
        done = False
        p_x, p_y = pos_dir

        if (p_x, p_y) in connections.keys():
            if connections[pos_dir] == 0:
                done = True
            if not move_boxes(walls, boxes, direction, pos_dir):
                return False

        if done:
            break

    change_coords(boxes, direction, pos)

    return True


def change_coords(boxes: set[tuple[int, int, int]], direction: int, pos: tuple[int, int]) -> None:
    connections = {(x, y): con for x, y, con in boxes}

    if connections[pos] == 0:
       x1, y1 = pos
       x2 = x1 + 1
       y2 = y1

    else:
       x2, y2 = pos
       x1 = x2 - 1
       y1 = y2

    dirs = [[(x1, y1 - 1, 0), (x2, y2 - 1, 1)], [(x1 + 1, y1, 0), (x2 + 1, y2, 1)], [(x1, y1 + 1, 0), (x2, y2 + 1, 1)], [(x1 - 1, y1, 0), (x2 - 1, y2, 1)]]

    boxes.remove((x1, y1, 0))
    boxes.remove((x2, y2, 1))
    boxes.add(dirs[direction][0])
    boxes.add(dirs[direction][1])


with open("day_15.txt") as f:
    walls: set[tuple[int, int]] = set()
    boxes: set[tuple[int, int, int]] = set()
    width = 0
    height = 0
    moves = ''
    mapping = True

    for y, line in enumerate(f):
        line = line.replace('\n', '')

        if line == '':
            mapping = False

        if mapping:
            height += 1
            width = len(line)

            for x, char in enumerate(line):
                if char == '#':
                    walls.add((2 * x, y))
                    walls.add((2 * x + 1, y))

                elif char == 'O':
                    boxes.add((2 * x, y, 0))
                    boxes.add((2 * x + 1, y, 1))

                elif char == '@':
                    pos = (2 * x, y)

        else:
            moves += line

boxes, pos = move(walls, boxes, moves, pos, height, width)

for y in range(height):
    line = ''
    for x in range(width * 2):
        if (x, y) in walls:
            line += '#'

        elif (x, y, 0) in boxes:
            line += '['

        elif (x, y, 1) in boxes:
            line += ']'

        elif (x, y) == pos:
            line += '@'

        else:
            line += '.'

    print(line)

result = 0

for x, y, side in boxes:
    if side == 0:
        result += 100 * y + x

print(result)
