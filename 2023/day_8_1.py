with open('day_8_test.txt') as f:
    data = f.read()
    data = data.split('\n')
    
dirs = data[0]
paths = {}
for i in range(len(data)):
    if i in [0,1]:
        continue
        
    loc_data = data[i].split(' = (')
    origin = loc_data[0]
    dest = loc_data[1].split(', ')
    dest[1] = dest[1].replace(')', '')
    paths[origin] = dest
    
i = 0
rounds = 0
curr_loc = 'AAA'
while True:
    rounds = rounds + 1
    loc_dirs = paths[curr_loc]
    
    if dirs[i] == 'L':
        curr_loc = loc_dirs[0]
        
    elif dirs[i] == 'R':
        curr_loc = loc_dirs[1]
        
    if curr_loc == 'ZZZ':
        print(rounds)
        break
        
    i = i + 1
    if i == len(paths):
        i = 0