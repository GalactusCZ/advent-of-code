with open('day_13_test.txt') as f:
    data = f.read()
    data = data.split('\n')

sections = []
curr_section = []
result= 0
for line in data:
    if line == '':
        sections.append(curr_section)
        curr_section = []

    else:
        curr_section.append(line)

sections.append(curr_section)
sc = 0
for sec in sections:
    sc += 1
    print('----------------')
    print(sc)
    # Base variables
    row_cache = []
    row_indexes = []
    row_reses = []
    row_res = 0

    # Goes through rows
    for i in range(len(sec)):
        # First val
        if i == 0:
            row_cache.append(sec[i])

        # If mirroring was found
        elif row_cache != [] and (sec[i] == row_cache[len(row_cache) - 1] or row_res != 0):
            # If mirroring end was reached
            if sec[i] != row_cache[len(row_cache) - 1]:
                row_reses.append(row_res)
                row_res = 0

                if i + 1 == len(sec):
                    row_cache = []
                else:
                    row_cache = [sec[i + 1]]
                continue

            row_res += 1

            # Set index when mirroring is detected
            if row_res == 1:
                row_indexes.append(i)

            row_cache.pop()

        # Appending cache
        else:
            row_cache.append(sec[i])

    print(row_indexes)
    print(row_reses)

    """
    columns = list(zip(*sec))

    # Base variables
    col_cache = []
    col_index = 0
    col_res = 0

    # Goes through cols
    for i in range(len(columns)):
        # First val
        if i == 0:
            col_cache.append(columns[i])

        # If mirroring was found
        elif col_cache != [] and (columns[i] == col_cache[len(col_cache) - 1] or col_res != 0):
            # If mirroring end was reached
            if columns[i] != col_cache[len(col_cache) - 1]:
                col_cache = []
                continue

            col_res += 1

            # Set index when mirroring is detected
            if col_res == 1:
                col_index = i

            col_cache.pop()

        # Appending cache
        else:
            if col_cache == [] and col_res != 0:
                break
            else:
                col_cache.append(columns[i])

    print(f"res row: {row_res}, col: {col_res}")
    print(f"index row: {row_index}, col: {col_index}")
    if row_res > col_res:
        print("R")
        curr_result = 100 * row_index
    else:
        print("C")
        curr_result = col_index
    print(curr_result)
    result += curr_result

print(result)
    """
