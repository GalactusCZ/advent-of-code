def get_num (engine: list[str], cords: list[int], directions: int) -> int:
    num = int(engine[cords[0]][cords[1]])

    if directions == 2:
        # left
        if 0 <= cords[1] - 1 and engine[cords[0]][cords[1] - 1].isdigit():
            num = num + (10 * get_num(engine, [cords[0], cords[1] - 1], 0))

        # right
        if len(engine[cords[0]]) > cords[1]+1 and engine[cords[0]][cords[1] + 1].isdigit():
            new_num = get_num(engine, [cords[0], cords[1] + 1], 1)

            new_str = str(new_num)

            if new_str[0] == "1" and engine[cords[0]][cords[1] + 1] == "0":
                new_str = "0" + new_str[1:]

            if num == 0:
                new_str = "1" + new_str

            else:
                new_str = str(num) + new_str

            num = int(new_str)

    # left
    if directions == 0:
        if 0 <= cords[1] - 1 and engine[cords[0]][cords[1] - 1].isdigit():
            num = num + (10 * get_num(engine, [cords[0], cords[1] - 1], 0))

    # right
    if directions == 1:
        if len(engine[cords[0]]) > cords[1]+1 and engine[cords[0]][cords[1] + 1].isdigit():
            new_num = get_num(engine, [cords[0], cords[1] + 1], 1)

            new_str = str(new_num)

            if new_str[0] == "1" and engine[cords[0]][cords[1] + 1] == "0":
                new_str = "0" + new_str[1:]

            if num == 0:
                new_str = "1" + new_str

            else:
                new_str = str(num) + new_str

            num = int(new_str)

    return num

with open('day_3.txt') as f:
    engine = f.read()

engine = engine.split('\n')

# finds special chars
spec = []
for x in range(len(engine)):
    for y in range(len(engine[x])):
        if engine[x][y] == "*":
            spec.append([x,y])

# goes through stars
valid_num = 0
for star in spec:
    numbers = []
    # up
    if engine[star[0] - 1][star[1]].isdigit():
        numbers.append([get_num(engine, [star[0] - 1, star[1]], 2)])
    else:
        if engine[star[0] - 1][star[1] - 1].isdigit():
            numbers.append([get_num(engine, [star[0] - 1, star[1] - 1], 0)])
        if engine[star[0] - 1][star[1] + 1].isdigit():
            numbers.append([get_num(engine, [star[0] - 1, star[1] + 1], 1)])

    # down
    if engine[star[0] + 1][star[1]].isdigit():
        numbers.append([get_num(engine, [star[0] + 1, star[1]], 2)])
    else:
        if engine[star[0] + 1][star[1] - 1].isdigit():
            numbers.append([get_num(engine, [star[0] + 1, star[1] - 1], 0)])
        if engine[star[0] + 1][star[1] + 1].isdigit():
            numbers.append([get_num(engine, [star[0] + 1, star[1] + 1], 1)])

    # left
    if engine[star[0]][star[1] - 1].isdigit():
        numbers.append([get_num(engine, [star[0], star[1] - 1], 0)])

    # right
    if engine[star[0]][star[1] + 1].isdigit():
        numbers.append([get_num(engine, [star[0], star[1] + 1], 1)])

    # sums numbers if possible
    if len(numbers) == 2:
        valid_num = valid_num + (numbers[0][0] * numbers[1][0])
    else:
        print(star)
        print(numbers)


print(valid_num)