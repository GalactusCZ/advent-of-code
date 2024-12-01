with open('day_16.txt') as f:
    data = f.read()
    data = data.split('\n')
    
new_data = []
for line in data:
    new_data.append(list(line))
    
data = new_data

starts = []
for i in range(len(data)):
    for j in range(len(data[0])):
        if i == 0:
            starts.append([[i,j], 's'])
        if i == len(data) - 1:
            starts.append([[i,j], 'n'])
        if j == 0:
            starts.append([[i,j], 'e'])
        if j == len(data[0]) - 1:
            starts.append([[i,j], 'w'])

results = []
rn = 0
for start in starts:
    rn += 1
    print(rn)
    pos = start[0]
    dir = start[1]
    energized = []
    to_go = [[pos, dir]]
    
    while to_go != []:
        tg = to_go[0]
        pos = tg[0]
        dir = tg[1]
        char = data[pos[0]][pos[1]]
        new_dir = ''
        new_dir2 = ''
        
        if char == '.':
            new_dir = dir
            
        elif char == '/':
            if dir == 'n':
                new_dir = 'e'
            elif dir == 'w':
                new_dir = 's'
            elif dir == 's':
                new_dir = 'w'
            elif dir == 'e':
                new_dir = 'n'
            
        elif char == '\\':
            if dir == 'n':
                new_dir = 'w'
            elif dir == 'w':
                new_dir = 'n'
            elif dir == 's':
                new_dir = 'e'
            elif dir == 'e':
                new_dir = 's'
                
        elif char == '-' and pos not in energized:
            if dir == 'w' or dir == 'e':
                new_dir = dir
            else:
                new_dir = 'w'
                new_dir2 = 'e'
                
        elif char == '|' and pos not in energized:
            if dir == 'n' or dir == 's':
                new_dir = dir
            else:
                new_dir = 'n'
                new_dir2 = 's' 
                
        # Insert in energized
        if pos not in energized:
            energized.append(pos)
       
        if (new_dir == 'n' or new_dir2 == 'n') and pos[0] - 1 >= 0:
            move = 1
            
            while pos[0] - move >= 0 and data[pos[0] - move][pos[1]] == '.':
                if [pos[0] - move, pos[1]] not in energized:
                    energized.append([pos[0] - move, pos[1]])
                move += 1
                
            if pos[0] - move >= 0:
                to_go.append([[pos[0] - move, pos[1]],'n'])
                
                
        if (new_dir == 'e' or new_dir2 == 'e') and pos[1] + 1 < len(data[0]):
            move = 1
            
            while pos[1] + move < len(data[0]) and data[pos[0]][pos[1] + move] == '.':
                if [pos[0], pos[1] + move] not in energized:
                    energized.append([pos[0], pos[1] + move])
                move += 1
                
            if pos[1] + move < len(data[0]):
                to_go.append([[pos[0], pos[1] + move],'e'])
                
                
        if (new_dir == 's' or new_dir2 == 's') and pos[0] + 1 < len(data):
            move = 1
            
            while pos[0] + move < len(data) and data[pos[0] + move][pos[1]] == '.':
                if [pos[0] + move, pos[1]] not in energized:
                    energized.append([pos[0] + move, pos[1]])
                move += 1
                
            if pos[0] + move < len(data):
                to_go.append([[pos[0] + move, pos[1]],'s'])
              
        if (new_dir == 'w' or new_dir2 == 'w') and pos[1] - 1 >= 0:
            move = 1
            
            while pos[1] - move >= 0 and data[pos[0]][pos[1] - move] == '.':
                if [pos[0], pos[1] - move] not in energized:
                    energized.append([pos[0], pos[1] - move])
                move += 1
                
            if pos[1] - move >= 0:
                to_go.append([[pos[0], pos[1] - move],'w'])
        
        to_go.pop(0)
        
    results.append(len(energized))

"""
prnt= [[] for x in range(len(data))]
for i in range(len(data)):
    for j in range(len(data[0])):
        if [i,j] in energized:
            prnt[i].append("#")
        else:
            prnt[i].append(".")
for p in prnt:
    print(p)
"""

print(max(results))