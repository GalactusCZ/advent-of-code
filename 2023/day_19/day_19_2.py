def pathing(paths: list[str], ranges: list[list[int]],index: int) -> int:
    # Gets operations
    operations = paths[index]
    curr_res= 0

    # Goes through operations
    for op in operations:
        # If operation has logic
        if ':' in op:
            op = op.split(':')
            val = int(op[0][2:])
            typ = op[0][0]
            sign = op[0][1]

            # Higher than
            if sign == '>' and val >= ranges[typ][0] and val < ranges[typ][1]:
                # New ranges
                new_ranges = {'x': [], 'm': [], 'a': [], 's': []}
                for k in ranges.keys():
                    for num in ranges[k]:
                        new_ranges[k].append(num)

                new_ranges[typ][0] = val + 1
                # Calculations
                calc = new_ranges[typ][1] - new_ranges[typ][0] + 1
                calc_res = {'x': ranges['x'][1] - ranges['x'][0] + 1, 'm': ranges['m'][1] - ranges['m'][0] + 1, 'a': ranges['a'][1] - ranges['a'][0] + 1, 's': ranges['s'][1] - ranges['s'][0] + 1}
                calc_res[typ] = calc

                # Accept
                if op[1] == 'A':

                    curr_res += calc_res['x'] * calc_res['m'] * calc_res['a'] * calc_res['s']

                # Reject
                elif op[1] == 'R':
                    pass

                # Continue deeper
                else:
                    # Recursion
                    curr_res += pathing(paths, new_ranges, op[1])


                # Remainder
                ranges[typ][1] = val

            # Lower than
            elif sign == '<' and val >= ranges[typ][0] + 1 and val < ranges[typ][1] + 1:
                # New ranges
                new_ranges = {'x': [], 'm': [], 'a': [], 's': []}
                for k in ranges.keys():
                    for num in ranges[k]:
                        new_ranges[k].append(num)

                new_ranges[typ][1] = val - 1
                # Calculations
                calc = new_ranges[typ][1] - new_ranges[typ][0] + 1
                calc_res = {'x': ranges['x'][1] - ranges['x'][0] + 1, 'm': ranges['m'][1] - ranges['m'][0] + 1, 'a': ranges['a'][1] - ranges['a'][0] + 1, 's': ranges['s'][1] - ranges['s'][0] + 1}
                calc_res[typ] = calc

                # Accept
                if op[1] == 'A':

                    curr_res += calc_res['x'] * calc_res['m'] * calc_res['a'] * calc_res['s']

                # Reject
                elif op[1] == 'R':
                    pass

                # Continue deeper
                else:
                    # Recursion
                    curr_res += pathing(paths, new_ranges, op[1])

                # Remainder
                ranges[typ][0] = val

        # Else it is used as value
        else:
            # Calculations
            calc_res = {'x': ranges['x'][1] - ranges['x'][0] + 1, 'm': ranges['m'][1] - ranges['m'][0] + 1, 'a': ranges['a'][1] - ranges['a'][0] + 1, 's': ranges['s'][1] - ranges['s'][0] + 1}

            # Accept
            if op == 'A':
                curr_res += calc_res['x'] * calc_res['m'] * calc_res['a'] * calc_res['s']


            # Reject
            elif op == 'R':
                pass

            # Continue deeper
            else:
                # Recursion
                curr_res += pathing(paths, ranges, op)

    return curr_res


with open('day_19.txt') as f:
    data = f.read().split('\n')

# Base variables
next = False
paths = {}

# Goes through lines
for line in data:
    # If line is empty, switch to origins
    if line == '':
        break

    # Captures paths
    line = line.split('{')
    line[1] = line[1][:len(line[1]) - 1]

    index = line[0]
    vals = line[1].split(',')

    paths[index] = vals

result= 0
ranges = {'x': [1,4000], 'm': [1,4000], 'a': [1,4000], 's': [1,4000]}
index = 'in'

#paths = {'in': ['x>2000:fx', 'A'], 'fx': ['A']}

result = pathing(paths, ranges, index)

print(result)