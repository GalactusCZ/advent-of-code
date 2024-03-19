with open('day_11_test2.txt') as f:
    data = f.read()
    data = data.split('\n')

s_data = []
for line in data:
    s_data.append(list(line))

# Create blank line
blank_line = []
for i in range(len(s_data[0])):
    blank_line.append('.')

# Find blank lines
i = 0
while True:
    if '#' not in s_data[i]:
        s_data.insert(i, blank_line)
        i = i + 1

    i = i + 1

    if i == len(s_data):
        break


# Find blank collums
i = 0
blank_cols = 0
while True:
    no_galaxy = True
    for j in range(len(s_data)):
        if s_data[j][i] == '#':
            no_galaxy = False

    if no_galaxy:
        blank_cols = blank_cols + 1

        for j in range(len(s_data)):
            if '#' in s_data[j]:
                s_data[j].insert(i, '.')
            else:
                s_data[j].insert(i, '.')

        i = i + 1



    i = i + 1

    if i == len(s_data[0]):
        break

# Solves some bsh happening with original blank lines
for i in range(len(s_data)):
    if '#' not in s_data[i] and len(s_data[i]) != len(s_data[0]):
        for j in range(blank_cols):
            s_data[i].pop()

"""
# Print
for dat in s_data:
    print(dat)
print('-----------------------------------------')
"""

# Find galaxies
galaxies = []
for y in range(len(s_data)):
    for x in range(len(s_data[0])):
        if s_data[y][x] == '#':
            galaxies.append([y, x])

# Result calculation
result = 0
move = 0
for i in range(len(galaxies)):
    j = move + 1

    while True:
        result = result + (abs(galaxies[i][0] - galaxies[j][0]) + abs(galaxies[i][1] - galaxies[j][1]))
        #print(f"i: {i}, j: {j}")

        j = j + 1

        if j == len(galaxies):
            move = move + 1
            break

    if move + 1 == len(galaxies):
        break

print(result)