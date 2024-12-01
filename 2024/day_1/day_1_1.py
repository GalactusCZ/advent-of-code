left: list[int] = []
right: list[int] = []

with open("day_1.txt") as file:
    for line in file:
        line = line.split("   ")
        left.append(int(line[0]))
        right.append(int(line[1]))

left.sort()
right.sort()
suma = 0

for i in range(len(left)):
    suma += abs(left[i] - right[i])

print(suma)