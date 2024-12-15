def move(walls: set[tuple[int, int]], boxes: set[tuple[int, int]], moves: str, pos: tuple[int, int], height: int, width: int) -> None:
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

        if next_pos in boxes:
            if move_boxes(walls, boxes, direction, next_pos, False):
                pos = next_pos

        elif next_pos not in walls:
            pos = next_pos

        # for y in range(height):
        #     line = ''
        #     for x in range(width):
        #         if (x, y) in walls:
        #             line += '#'

        #         elif (x, y) in boxes:
        #             line += 'O'

        #         elif (x, y) == pos:
        #             line += '@'

        #         else:
        #             line += '.'

        #     print(line)


def move_boxes(walls: set[tuple[int, int]], boxes: set[tuple[int, int]], direction: int, pos: tuple[int, int], recursive: bool) -> bool:
    x, y = pos
    pos_dirs = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]

    if pos_dirs[direction] in boxes:
        if move_boxes(walls, boxes, direction, pos_dirs[direction], True):
            if not recursive:
                boxes.remove(pos)

            return True

    elif pos_dirs[direction] not in walls:
        boxes.add(pos_dirs[direction])
        
        if not recursive:
            boxes.remove(pos)
        return True

    return False


with open("day_15.txt") as f:
    walls: set[tuple[int, int]] = set()
    boxes: set[tuple[int, int]] = set()
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
                    walls.add((x, y))

                elif char == 'O':
                    boxes.add((x, y))

                elif char == '@':
                    pos = (x, y)

        else:
            moves += line

move(walls, boxes, moves, pos, height, width)

result = 0

for box in boxes:
    x, y = box

    result += 100 * y + x

print(result)
