safe = 0

def check(line: list[int], fails: int, index: int, rising: bool) -> bool:
    if index == len(line):
        return True

    if index == 1:
        if line[0] == line[1]:
            pass
        else:
            return check(line, fails, index + 1, line[0] )

with open("day_2.txt") as file:
    for line in file:
        line = line.split(" ")
        line = [int(num) for num in line]

        retrieve = check(line, 1, 1, True)


