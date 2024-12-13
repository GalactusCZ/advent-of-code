def check_machines(machine: dict[str, int]) -> int:
    p_x, p_y = machine['P']
    a_x, a_y = machine['A']
    b_x, b_y = machine['B']
    b = 0

    for b in range(min(p_x // b_x, p_y // b_y) + 1):
        for a in range(min(p_x // a_x, p_y // a_y) + 1):
            if b * b_x + a * a_x == p_x and b * b_y + a * a_y == p_y:
                return b + a * 3

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
            
            curr_m['P'] = (int(line[0].split('=')[1]), int(line[1].split('=')[1]))

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