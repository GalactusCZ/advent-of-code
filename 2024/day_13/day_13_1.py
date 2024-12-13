def check_machines(machine: dict[str, int]) -> int:
    p_x, p_y = machine['P']
    a_x, a_y = machine['A']
    b_x, b_y = machine['B']
    b = 0
    
    while b * b_x <= p_x and b * b_y <= p_y:
        if p_x == b_x * b and p_y == b_y * b:
            return b

        a = 0
        while a * a_x <= p_x and a * a_y <= p_y:
            if p_x == a_x * a + b_x * b and p_y == a_y * a + b_y * b:
                return b + a * 3

            a += 1

        b += 1

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

    result = 0

    for machine in machines:
        test = check_machines(machine)
        print(test, machine)
        result += test

    print(result)