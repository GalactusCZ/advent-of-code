def check_machines()

with open("day_13_test.txt") as f:
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
            
    for machine in machines:
            p_x, p_y = machine['P']
            a_x, a_y = machine['A']
            b_x, b_y = machine['B']
            
            for a in range(101):
                
                
                for b in range(1, 101):
            