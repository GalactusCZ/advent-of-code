def move(line: list[str]) -> list[str]:
    # Base variables
    pos = 0
    
    # Go through chata
    for i in range(len(line)):
        # Movable rock
        if line[i] == "O":
            # If already on the right position
            if i != pos:
                line[i] = "."
                line[pos] = "O"

                pos += 1

            else:
                pos += 1

        # Unmovable rock
        elif line[i] == '#':
            pos = i + 1

    return line

def calc(line: list[str]) -> int:
    # Base variables
    curr_result = 0
    
    for i in range(len(line)):
        if line[i] == 'O':
            curr_result += len(line) - i

    return curr_result


with open('day_14.txt') as f:
    data = f.read()
    data = data.split('\n')
    
data = list(zip(*data))

result = 0
ln = 0
for line in data:
    ln += 1
    print("---------------")
    print(ln)
    # Tuple to list
    line = list(line)

    # Move
    line = move(line)

    # Calculate
    curr_res = calc(line)

    print(curr_res)

    result += curr_res

print(result)