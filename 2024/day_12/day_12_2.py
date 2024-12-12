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


def count_corners(pos: tuple[int, int], char: str, start: tuple[int, int], direction: int, check: int, map_plot: list[str]) -> int:
    dirs = [(x. y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    dx, dy = dirs[check]

    if not is_valid(dirs[check], len(map_plot), len(map_plot[0])) or map_plot[dy][dx] != char:
        


with open("day_12_test.txt") as f:
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
            print(start, this_block(starts[start], start, plot_map, used))

    print(result)