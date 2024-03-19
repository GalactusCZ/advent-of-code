with open('day_11.txt') as f:
    data = f.read()
    data = data.split('\n')

s_data = []
for line in data:
    s_data.append(list(line))

# Find blank lines
i = 0
blank_lines = []
while True:
    if '#' not in s_data[i]:
        blank_lines.append(i)

    i = i + 1

    if i == len(s_data):
        break

# Find blank collums
i = 0
blank_cols = []
while True:
    no_galaxy = True
    for j in range(len(s_data)):
        if s_data[j][i] == '#':
            no_galaxy = False

    if no_galaxy:
        blank_cols.append(i)

    i = i + 1

    if i == len(s_data[0]):
        break

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

print(galaxies)
print(blank_cols)
print(blank_lines)
# Result calculation
result = 0
move = 0
for i in range(len(galaxies)):
    j = move + 1

    while True:
        w_adder = 0
        print(f"i: {i}, j: {j}")
        for bc in blank_cols:
            #print(f"bc: {bc} in {range(min(galaxies[i][1],galaxies[j][1]), max(galaxies[i][1],galaxies[j][1]))}")
            if bc in range(min(galaxies[i][1],galaxies[j][1]), max(galaxies[i][1],galaxies[j][1])):
                w_adder = w_adder + 999999

        h_adder = 0
        for bl in blank_lines:
            #print(f"bl: {bl} in {range(min(galaxies[i][0], galaxies[j][0]), max(galaxies[i][0], galaxies[j][0]))}")
            if bl in range(min(galaxies[i][0], galaxies[j][0]), max(galaxies[i][0], galaxies[j][0])):
                h_adder = h_adder + 999999

        width = abs(galaxies[i][1] - galaxies[j][1]) + w_adder
        height = abs(galaxies[i][0] - galaxies[j][0]) + h_adder
        result = result + (width + height)
        #print(f"i: {i}, j: {j}")

        j = j + 1

        if j == len(galaxies):
            move = move + 1
            break

    if move + 1 == len(galaxies):
        break

print(result)