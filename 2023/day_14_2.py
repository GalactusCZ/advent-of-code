import timeit

start = timeit.default_timer()

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

def rev_rotate(data: list[list[str]]) -> list[list[str]]:
    # Reverse data
    new_data = []
    for line in data:
        # To list
        line = list(line)
        # Reversed list
        line.reverse()
        new_data.append(line)

    data = new_data

    # Rotate
    new_data = [[] for i in range(len(data[0]))]
    # Go through lines
    for line in data:
        # Go through chars
        for i in range(len(line)):
            new_data[i].append(line[i])

    return new_data

def rotate(data: list[list[str]]) -> list[tuple[str]]:
    # Reverse data
    data = list(zip(*data))

    new_data = []
    for line in data:
        line = list(line)
        line.reverse()

        new_data.append(line)

    return new_data

with open('day_14.txt') as f:
    data = f.read()
    data = data.split('\n')

orig_data = rev_rotate(rev_rotate(data))
size = len(data)

# Rounds
cache = {}
second_cache = {}
res_appear = {}
res_difs = {}
data = orig_data
rounds = 1000
rn = 0
for round in range(rounds):
    rn += 1
    # All rotations
    str_data = [''.join(x) for x in data]
    str_data = ''.join(str_data)
    if str_data in second_cache.keys():
        data = second_cache[str_data]
    else:
        repet = 0
        for r in range(4):
            # Rotate data
            start_r = timeit.default_timer()
            data = rotate(data)
            stop_r = timeit.default_timer()

            result = 0
            new_data = []
            start_m = timeit.default_timer()
            for line in data:
                # Tuple to list
                pre_line = list(line)
                str_line = ''.join(pre_line)

                if str_line in cache.keys():
                    line = cache[str_line]
                else:
                    # Move
                    line = move(pre_line)
                    cache[str_line] = line


                new_data.append(line)

            stop_m = timeit.default_timer()

            data = new_data


            # If end is reached
            if round + 1 == rounds and r == 3:
                data = rotate(data)

                # Calculate
                for line in data:
                    curr_res = calc(line)

                    result += curr_res



        second_cache[str_data] = data
    # Calculate
    spec_data = rotate(data)
    curr_res = 0
    for line in spec_data:
        curr_res += calc(line)

    print(rn)
    if str(curr_res) not in res_appear.keys():
        res_appear[str(curr_res)] = rn
    else:
        dif = rn - res_appear[str(curr_res)]

        if str(curr_res) not in res_difs.keys():
            res_difs[str(curr_res)] = []

        change_dif = res_difs[str(curr_res)]
        change_dif.append(dif)
        res_difs[str(curr_res)] = change_dif

        res_appear[str(curr_res)] = rn

    if curr_res == 105620:
        print(f"curr: {curr_res}")

print(f"Move: {stop_m - start_m}, Rotation: {stop_r - start_r}")

keys = []
for key in res_appear.keys():
    keys.append(key)

keys = sorted(keys)

for key in keys:
    if key in res_difs.keys():
        print(f"k: {key}, appear: {res_appear[key]}, difs: {res_difs[key]}")

# Time measurement
stop = timeit.default_timer()
print('Time: ', stop - start)