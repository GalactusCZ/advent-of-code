with open("day_9.txt") as f:
    line = f.readline()
    converted: list[str] = []
    index = 0
    space = False

    for char in line:
        if not space:
            for _ in range(int(char)):
                converted.append(str(index))

            index += 1
            space = True

        else:
            for _ in range(int(char)):
                converted.append('.')

            space = False

    result = 0
    index = 0

    while len(converted) > 0:
        if converted[0] == '.':
            while len(converted) > 1 and \
                  converted[len(converted) - 1] == '.':
                converted = converted[:len(converted) - 1]

            if len(converted) > 1:
                result += index * int(converted[len(converted) - 1])
                converted = converted[:len(converted) - 1]


        else:
            result += index * int(converted[0])

        converted = converted[1:]
        index += 1

    print(result)
