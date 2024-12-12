def is_valid(pos: tuple[int, int], height: int, width: int) -> bool:
    x, y = pos
    return 0 <= x < width and 0 <= y < height

def this_block(char: str, pos: tuple[int, int], plot_map: list[str], used: set[tuple[int, int]]) -> set[tuple[int, int]]:
    x, y = pos
    dif_pos = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    block = set([pos])
    used.add(pos)

    for dif in dif_pos:
        dx, dy = dif

        if 0 <= dx < len(plot_map[0]) and 0 <= dy < len(plot_map) and plot_map[dy][dx] == char and dif not in used:
            block.update(this_block(char, dif, plot_map, used))

    return block


def count_sides(block: set[tuple[int, int]]) -> int:
    sides = 0
    ys = [y for _, y in block]
    xs = [x for x, _ in block]
        
    for y in range(min(ys), max(ys) + 1):
        prev_top = False
        prev_bot = False
        for x in range(min(xs), max(xs) + 1):
            if (x, y) in block:
                if (x, y - 1) not in block:
                    if not prev_top:
                        sides += 1
                        prev_top = True
                else:
                    prev_top = False
 
                if (x, y + 1) not in block:
                    if not prev_bot:
                        sides += 1
                        prev_bot = True
                else:
                    prev_bot = False
                    
            else:
                prev_top = False
                prev_bot = False
        
    for x in range(min(xs), max(xs) + 1):
        prev_l = False
        prev_r = False
        for y in range(min(ys), max(ys) + 1):
            if (x, y) in block:
                if (x - 1, y) not in block:
                    if not prev_l:
                        sides += 1
                        prev_l = True
                else:
                    prev_l = False
 
                if (x + 1, y) not in block:
                    if not prev_r:
                        sides += 1
                        prev_r = True
                else:
                    prev_r = False
                    
            else:
                 prev_l = False
                 prev_r = False
             
    return sides


with open("day_12.txt") as f:
    plot_map: list[str] = []
    starts: dict[tuple[int, int], str] = {}
    prev_char = '.'

    for y, line in enumerate(f):
        line = line.replace('\n', '')
        plot_map.append(line)

        for x, char in enumerate(line):
            if char != prev_char:
                starts[(x, y)] = char
                prev_char = char

    used: set[tuple[int, int]] = set()
    result = 0

    for start in starts.keys():
        if start not in used:
            block = this_block(starts[start], start, plot_map, used)
            sides = count_sides(block)
            print(start, len(block), sides)
            result += len(block) * sides

    print(result)