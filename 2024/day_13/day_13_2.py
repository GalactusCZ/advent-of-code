def check_machines(machine: dict[str, int]) -> int:
    p_x, p_y = machine['P']
    a_x, a_y = machine['A']
    b_x, b_y = machine['B']
    b = 0
    g_change = 0
    changes = 0
    offset = 0
    amount = 0

    for b in range(min(p_x // b_x, p_y // b_y) + 1):
        if b > 10000000 and changes == 0:
            return 0

        if (p_x - b * b_x) % a_x == 0 and \
           (p_y - b * b_y) % a_y == 0:
            changes += 1

            if changes == 1:
                offset = b - g_change

            elif changes == 2:
                amount = b - g_change
                break

            g_change = b

            if (p_x - b * b_x) // a_x == (p_y - b * b_y) // a_y:
                return b + ((p_x - b * b_x) // a_x) * 3

    print(offset, amount)
    x_div_a = (p_x - offset * b_x) // a_x
    y_div_a = (p_y - offset * b_y) // a_y
    x_a_dif = x_div_a - (p_x - (offset + amount) * b_x) // a_x
    y_a_dif = y_div_a - (p_y - (offset + amount) * b_y) // a_y
    timer = 10000000000000
    times = 0
    x_higher = True

    if x_div_a < y_div_a:
        x_higher = False

    if (x_higher and x_a_dif < y_a_dif) or (not x_higher and x_a_dif > y_a_dif):
        return 0

    # print(x_div_a, y_div_a)
    # print(x_a_dif, y_a_dif)

    while timer > 0:
        x_calc = x_div_a - (timer + times) * x_a_dif
        y_calc = y_div_a - (timer + times) * y_a_dif
        if x_calc < 0 or y_calc < 0 or (x_higher and x_calc < y_calc) or (not x_higher and x_calc > y_calc):
            timer //= 10

        elif x_calc == y_calc:
            times += timer
            b_times = offset + times * amount
            a_times = (p_x - b_times * b_x) // a_x
            # print(b_times * b_x + a_times * a_x)
            return b_times + a_times * 3

        else:
            times += timer

    # print(x_calc, y_calc)

    # last_x = 0
    # last_y = 0

    # for b in range(offset, min(p_x // b_x, p_y // b_y) + 1, amount):
    #     if (p_x - b * b_x) % a_x == 0 and \
    #        (p_y - b * b_y) % a_y == 0:
    #         print(last_x - ((p_x - b * b_x) // a_x), last_y - ((p_y - b * b_y) // a_y))
    #         last_x = ((p_x - b * b_x) // a_x)
    #         last_y = ((p_y - b * b_y) // a_y)
    #         print(last_x, last_y)

    #         if (p_x - b * b_x) // a_x == (p_y - b * b_y) // a_y:
    #             return b + ((p_x - b * b_x) // a_x) * 3

    return 0


with open("day_13.txt") as f:
    machines: list[dict[str, int]] = []
    curr_m: dict[str, int] = {}
    
    for line in f:
        line = line.replace('\n', '')
        
        if line == '':
            machines.append(curr_m)
            curr_m = {}
            
        elif line[0] == 'P':
            line = line.split(': ')
            line = line[1].split(', ')
            
            curr_m['P'] = (int(line[0].split('=')[1]) + 10000000000000, int(line[1].split('=')[1]) + 10000000000000)

        else:
            spliter = line.replace('Button ', '')
            spliter = spliter.split(': ')
            line = spliter[1].split(', ')

            curr_m[spliter[0]] = (int(line[0].split('+')[1]), int(line[1].split('+')[1]))

    machines.append(curr_m)
    result = 0

    for machine in machines:
        test = check_machines(machine)
        print(test, machine)
        result += test

    print(result)