Divided = list[tuple[int, int, int]]

def calculate(files: list[Divided], spaces: list[Divided]) -> int:
    result = 0

    for i, (f_amount, f_index, f_ci) in enumerate(files):
        for j, (s_amount, s_index, s_ci) in enumerate(spaces):
            if f_ci < s_ci:
                spaces = spaces[:j]
                break
                
            if s_amount >= f_amount:


with open("day_9_test.txt") as f:
    line = f.readline()
    files: list[Divided] = []
    spaces: list[Divided] = []
    c_index = 0
    index = 0

    for i, char in enumerate(line):
        if i % 2 == 0:
            files.append((int(char), index, c_index))
            index += 1

        else:
            spaces.append((int(char), -1, c_index))
            
        c_index += int(char)

    files.reverse()
    print(calculate(files, spaces))