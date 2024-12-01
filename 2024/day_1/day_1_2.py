left: list[int] = []
right: dict[int, int] = {}

with open("day_1.txt") as file:
    for line in file:
        line = line.split("   ")
        left.append(int(line[0]))

        right_i = int(line[1])

        if right_i not in right.keys():
            right[right_i] = 1

        else:
            right[right_i] += 1

suma = 0

for num in left:
    if num in right.keys():
        suma += num * right[num]

print(suma)