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
    sc = sc + 1
    print('---------------------')
    print(sc)
    columns = ['' for i in range(len(sec[0]))]

    # Lines
    line_cache = []
    ref_scores = []
    ref_indexes = []
    curr_score = 0
    for i in range(len(sec)):
        # Updates columns list
        for j in range(len(sec[i])):
            columns[j] = columns[j] + sec[i][j]

        # Adds score if line in cache
        if curr_score != 0:
            rev_cache = line_cache
            rev_cache.reverse()
            if curr_score < len(rev_cache) and rev_cache[curr_score] == sec[i]:
                curr_score = curr_score + 1

            else:
                ref_scores.append(curr_score)
                line_cache = [sec[i]]
                curr_score = 0

        # Detects mirroring
        elif line_cache != [] and sec[i] == line_cache[len(line_cache) - 1]:
            ref_indexes.append(i)
            curr_score = 1

        # Appends cache
        else:
            line_cache.append(sec[i])

    if curr_score != 0:
        ref_scores.append(curr_score)

    if ref_indexes != []:
        line_res = ref_indexes[ref_scores.index(max(ref_scores))]
        line_score = max(ref_scores)

    else:
        line_res = 0
        line_score = 0

    # Column
    col_cache = []
    ref_scores = []
    ref_indexes = []
    curr_score = 0
    for i in range(len(columns)):
        # Adds score if line in cache
        if curr_score != 0:
            rev_cache = col_cache
            rev_cache.reverse()
            if curr_score < len(rev_cache) and rev_cache[curr_score] == columns[i]:
                curr_score = curr_score + 1

            else:
                print(curr_score)
                ref_scores.append(curr_score)
                col_cache = [columns[i]]
                curr_score = 0

        if col_cache != [] and columns[i] == col_cache[len(col_cache) - 1]:
            ref_indexes.append(i)
            curr_score = 1

        else:
            col_cache.append(columns[i])

    if curr_score != 0:
        ref_scores.append(curr_score)

    if ref_indexes != []:
        col_res = ref_indexes[ref_scores.index(max(ref_scores))]
        col_score = max(ref_scores)

    else:
        col_res = 0
        col_score = 0

    print(f"score col: {col_score}, line: {line_score}")
    print(f"res col: {col_res}, line: {line_res}")
    if col_score > line_score:
        curr_res = col_res
    else:
        curr_res = line_res * 100

    result = result + curr_res
    print(curr_res)

print(result)