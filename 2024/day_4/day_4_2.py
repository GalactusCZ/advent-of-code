with open("day_4.txt") as f:
    lines: list[str] = []

    for line in f:
        lines.append(line.replace('\n', ''))

def search(coords: tuple[int, int], lines: list[str]) -> int:
    count = 0
    x, y = coords
    dirs = [(x - 1, y - 1), (x + 1, y + 1),
            (x + 1, y - 1), (x - 1, y + 1)]

    for i, dir in enumerate(dirs):
        x, y = dir
        if i % 2 == 0:
            ox, oy = dirs[i + 1]
        else:
            ox, oy = dirs[i - 1]

        if 0 <= x < len(lines[0]) and \
           0 <= ox < len(lines[0]) and \
           0 <= y < len(lines) and \
           0 <= oy < len(lines) and \
           lines[y][x] == 'M' and lines[oy][ox] == 'S':
            count += 1

    if count == 2:
        return 1

    return 0


amount = 0

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'A':
            adder = search((x, y), lines)
            amount += adder

print(amount)
