with open("day_4.txt") as f:
    lines: list[str] = []

    for line in f:
        lines.append(line.replace('\n', ''))

def search(coords: tuple[int, int], lines: list[str]) -> int:
    amount = 0
    letters = ['M', 'A', 'S']

    x, y = coords
    dirs = [[(x, y - num) for num in range(1, 4)],
            [(x + num, y) for num in range(1, 4)],
            [(x, y + num) for num in range(1, 4)],
            [(x - num, y) for num in range(1, 4)],
            [(x + num, y - num) for num in range(1, 4)],
            [(x + num, y + num) for num in range(1, 4)],
            [(x - num, y + num) for num in range(1, 4)],
            [(x - num, y - num) for num in range(1, 4)]]

    for dir in dirs:
        count = 0
        for i, (x, y) in enumerate(dir):
            if 0 <= x < len(lines[0]) and 0 <= y < len(lines) and lines[y][x] == letters[i]:
                count += 1

                if count == 3:
                    amount += 1

            else:
                break

    return amount

amount = 0

for y, line in enumerate(lines):
    for x, char in enumerate(line):
        if char == 'X':
            amount += search((x, y), lines)

print(amount)
