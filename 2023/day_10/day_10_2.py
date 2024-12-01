import numpy as np

def get_valid(x: int, y: int, map) -> bool:
    valid = ''
    # North
    if y - 1 >= 0 and (map[y - 1, x] == '7' or map[y - 1, x] == '|' or map[y - 1, x] == 'F' or map[y - 1, x] == 'S') and (map[y, x] == 'J' or map[y, x] == '|' or map[y, x] == 'L' or map[y, x] == 'S'):
        valid = valid + 'n'

    # East
    if x + 1 < len(map[0]) and (map[y, x + 1] == '7' or map[y, x + 1] == '-' or map[y, x + 1] == 'J' or map[y, x + 1] == 'S') and (map[y, x] == 'L' or map[y, x] == '-' or map[y, x] == 'F' or map[y, x] == 'S'):
        valid = valid + 'e'

    # South
    if y + 1 < len(map) and (map[y + 1, x] == 'J' or map[y + 1, x] == '|' or map[y + 1, x] == 'L' or map[y + 1, x] == 'S') and (map[y, x] == '7' or map[y, x] == '|' or map[y, x] == 'F' or map[y, x] == 'S'):
        valid = valid + 's'

    # West
    if x - 1 >= 0 and (map[y, x - 1] == 'L' or map[y, x - 1] == '-' or map[y, x - 1] == 'F' or map[y, x - 1] == 'S') and (map[y, x] == '7' or map[y, x] == '-' or map[y, x] == 'J' or map[y, x] == 'S'):
        valid = valid + 'w'

    return valid

with open('day_10.txt') as f:
    data = f.read()
    data = data.split('\n')

    new_data = []
    for line in data:
        new_data.append(list(line))

    np_data = np.array(new_data)

# Find start
s_y, s_x = None, None
for y in range(len(np_data)):
    for x in range(len(np_data[y])):
        if np_data[y, x] == 'S':
            s_y = y
            s_x = x
            break

    if s_y != None:
        break

# Gets the full loop
orig_path = get_valid(s_x, s_y, np_data)
dir = orig_path[0]
y = s_y
x = s_x
loop_cords = []
while True:
    if dir == 'n':
        y = y - 1
    elif dir == 'e':
        x = x + 1
    elif dir == 's':
        y = y + 1
    elif dir == 'w':
        x = x - 1

    paths = get_valid(x, y, np_data)


    if dir == 'n':
        dir = paths.replace('s', '')
    elif dir == 'e':
        dir = paths.replace('w', '')
    elif dir == 's':
        dir = paths.replace('n', '')
    elif dir == 'w':
        dir = paths.replace('e', '')

    loop_cords.append([y, x])

    if np_data[y, x] == 'S':
        break

start_path = get_valid(s_x, s_y, np_data)
if 'n' in start_path and 's' in start_path:
    start_char = '|'
elif 'w' in start_path and 'e' in start_path:
    start_char = '-'
elif 'n' in start_path and 'e' in start_path:
    start_char = 'L'
elif 'n' in start_path and 'w' in start_path:
    start_char = 'J'
elif 's' in start_path and 'e' in start_path:
    start_char = 'F'
elif 's' in start_path and 'w' in start_path:
    start_char = '7'

np_data[s_y, s_x] = start_char

# Validates
ins, outs, loop_ins, loop_outs = [], [], [], []
for y in range(len(np_data)):
    for x in range(len(np_data[y])):
        if [y, x] not in loop_cords:
            if y == 0:
                outs.append([y,x])

            elif [y - 1, x] in ins or [y - 1, x] in loop_ins:
                ins.append([y,x])

            elif [y - 1, x] in outs or [y - 1, x] in loop_outs:
                outs.append([y,x])

        else:
            if np_data[y,x] == '-':
                if y == 0:
                    loop_ins.append([y,x])

                elif [y - 1, x] in ins or [y - 1, x] in loop_ins:
                    loop_outs.append([y,x])

                elif [y - 1, x] in outs or [y - 1, x] in loop_outs:
                    loop_ins.append([y,x])

            elif np_data[y,x] == '|' or np_data[y,x] == 'F' or np_data[y,x] == '7':
                if y == 0:
                    loop_outs.append([y,x])

                elif [y - 1, x] in ins or [y - 1, x] in loop_ins:
                    loop_ins.append([y,x])

                elif [y - 1, x] in outs or [y - 1, x] in loop_outs:
                    loop_outs.append([y,x])

            elif np_data[y,x] == 'L':
                loc_y = y

                while True:
                    loc_y = loc_y - 1

                    if np_data[loc_y, x] == 'F':
                        if [loc_y, x] in loop_ins:
                            loop_ins.append([y,x])
                            break
                        elif [loc_y, x] in loop_outs:
                            loop_outs.append([y,x])
                            break

                    if np_data[loc_y, x] == '7':
                        if [loc_y, x] in loop_ins:
                            loop_outs.append([y,x])
                            break
                        elif [loc_y, x] in loop_outs:
                            loop_ins.append([y,x])
                            break

            elif np_data[y,x] == 'J':
                loc_y = y

                while True:
                    loc_y = loc_y - 1

                    if np_data[loc_y, x] == 'F':
                        if [loc_y, x] in loop_ins:
                            loop_outs.append([y,x])
                            break
                        elif [loc_y, x] in loop_outs:
                            loop_ins.append([y,x])
                            break

                    if np_data[loc_y, x] == '7':
                        if [loc_y, x] in loop_ins:
                            loop_ins.append([y,x])
                            break
                        elif [loc_y, x] in loop_outs:
                            loop_outs.append([y,x])
                            break


print(ins)
print(len(ins))