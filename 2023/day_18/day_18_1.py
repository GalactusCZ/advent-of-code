with open('day_18.txt') as f:
    data = f.read().split('\n')

pos = [0, 0]
poses = []
poses.append([0,0])

for line in data:
    line = line.split(' ')
    num = int(line[1])
    dir = line[0]

    for i in range(num):
        curr_pos = poses[len(poses) - 1]

        if dir == 'U':
            curr_pos[0] -= 1
        elif dir == 'R':
            curr_pos[1] += 1
        elif dir == 'D':
            curr_pos[0] += 1
        elif dir == 'L':
            curr_pos[1] -= 1

        poses.append([curr_pos[0], curr_pos[1]])

poses.pop()
max_y,max_x,min_y,min_x = 0,0,0,0
for ps in poses:
    if ps[0] > max_y:
        max_y = ps[0]
    if ps[0] < min_y:
        min_y = ps[0]
    if ps[1] > max_x:
        max_x = ps[1]
    if ps[1] < min_x:
        min_x = ps[1]

data = []

for i in range(min_y, max_y + 1):
    data.append([])
    index = len(data) - 1

    for j in range(min_x, max_x + 1):
        if [i,j] in poses:
            data[index].append('#')
        else:
            data[index].append('.')
"""
for d in data:
    print(d)
"""

for i in range(len(data)):
    mult = ''
    inner = False
    for j in range(len(data[0])):
        if data[i][j] == '#':
            change = False

            if (j == 0 or data[i][j - 1] != '#') and (j == len(data[0]) - 1 or data[i][j + 1] != '#'):
                change = True
            elif j == 0 or data[i][j - 1] != '#':
                if i > 0 and data[i - 1][j] == '#':
                    mult = 'u'
                else:
                    mult = 'd'
            elif j == len(data[0]) - 1 or data[i][j + 1] != '#':
                if mult == 'u':
                    if data[i - 1][j] == '#':
                        change = False
                    else:
                        change = True
                elif mult == 'd':
                    if data[i + 1][j] == '#':
                        change = False
                    else:
                        change = True

            if change:
                if inner:
                    inner = False
                else:
                    inner = True



        elif data[i][j] == '.':
            if inner:
                data[i][j] = 'O'

result = 0
for d in data:
    result += d.count('#') + d.count('O')
    print(d)

print(result)