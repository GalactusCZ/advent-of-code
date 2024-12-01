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
    print(valid)
    print(f"y: {y}, x: {x}")
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
       
length = 1
orig_path = get_valid(s_x, s_y, np_data)
dir = orig_path[0]
y = s_y
x = s_x
print(dir)
print(f"y: {y}, x: {x}")
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
    
    if np_data[y, x] == 'S':
        break
        
    length = length + 1
    
print(length / 2)