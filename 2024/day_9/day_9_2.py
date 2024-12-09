Divided = list[tuple[int, bool, int]]

def reorder(divided: Divided) -> Divided:
    end: Divided = []
    start: Divided = []
    curr_divided = divided.copy()

    while len(curr_divided) > 1:
        amount, is_num, mult = curr_divided.pop()

        if not is_num:
            end.append((amount, is_num, mult))

        else:
            changes = False

            while not changes and len(curr_divided) > 0:
                in_amount, in_is_num, _ = curr_divided[0]

                if in_is_num:
                    start.append(curr_divided[0])
                else:
                    if in_amount >= amount:
                        changes = True
                        start.append((amount, True, mult))

                        if in_amount > amount:
                            start.append((in_amount - amount, False, -1))

                    else:
                        start.append(curr_divided[0])

                curr_divided = curr_divided[1:]

            if changes:
                end.append((amount, False, -1))

            else:
                end.append((amount, True, mult))

            start.extend(curr_divided)
            curr_divided = start
            start = []

    end.reverse()
    return end


with open("day_9_test.txt") as f:
    line = f.readline()
    divided: Divided = []
    multiplier = 0

    for i, char in enumerate(line):
        if i % 2 == 0:
            divided.append((int(char), True, multiplier))
            multiplier += 1

        else:
            divided.append((int(char), False, -1))


    reor = reorder(divided)
    print(reor)

    stringify = ''
    for amount, is_num, mult in reor:
        for _ in range(amount):
            if is_num:
                stringify += str(mult)

            else:
                stringify += '.'

    print(stringify)

