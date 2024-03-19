from math import lcm

with open('day_8.txt') as f:
    data = f.read()
    data = data.split('\n')

# Get paths into dictionary
dirs = data[0]
starts,goals = [],[]
paths = {}
for i in range(len(data)):
    if i in [0,1]:
        continue

    loc_data = data[i].split(' = (')
    origin = loc_data[0]
    if origin[2] == "A":
        starts.append(origin)
    elif origin[2] == "Z":
        goals.append(origin)
    dest = loc_data[1].split(', ')
    dest[1] = dest[1].replace(')', '')
    paths[origin] = dest

rounds_list = []

for curr_loc in starts:
    i = 0
    rounds = 0
    while True:
        rounds = rounds + 1
        loc_dirs = paths[curr_loc]

        if dirs[i] == 'L':
            curr_loc = loc_dirs[0]

        elif dirs[i] == 'R':
            curr_loc = loc_dirs[1]

        if curr_loc in goals:
            rounds_list.append(rounds)
            break

        i = i + 1
        if i == len(dirs):
            i = 0
print(starts)
print(goals)
print(rounds_list)
max_val = max(rounds_list)
result = lcm(rounds_list[0],rounds_list[1],rounds_list[2],rounds_list[3],rounds_list[4],rounds_list[5])
print(result)