def plot_size(char: str, pos: tuple[int, int], plot_map: list[str], used: set[tuple[int, int]]) -> tuple[int, int]:
    x, y = pos
    dif_pos = [(x, y - 1), (x + 1, y), (x, y + 1), (x - 1, y)]
    fences = 0
    amount = 1
    used.add(pos)

    for dif in dif_pos:
        dx, dy = dif

        if not (0 <= dx < len(plot_map[0]) and 0 <= dy < len(plot_map)) or \
           plot_map[dy][dx] != char:
            fences += 1

        elif dif not in used:
            new_fences, new_amount = plot_size(char, dif, plot_map, used)
            fences += new_fences
            amount += new_amount

    return (fences, amount)


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
            fences, amount = plot_size(starts[start], start, plot_map, used)
            result += fences * amount

    print(result)