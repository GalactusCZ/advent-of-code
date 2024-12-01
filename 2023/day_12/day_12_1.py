with open('day_12.txt') as f:
    data = f.read()
    data = data.split('\n')

result = 0
ln = 0
for line in data:
    ln = ln + 1
    print(ln)
    line = line.split(' ')

    nums = line[1].split(',')
    nums = [int(x) for x in nums]

    chars = list(line[0])

    unknowns = []
    for i in range(len(chars)):
        if chars[i] == "?":
            unknowns.append(i)

    varieties = []
    runs = 0
    while unknowns != []:
        if runs == 0:
            test_chars1 = []
            test_chars2 = []
            for ch in chars:
                test_chars1.append(ch)
                test_chars2.append(ch)

            test_chars1[unknowns[0]] = '.'
            varieties.append(test_chars1)
            test_chars2[unknowns[0]] = '#'
            varieties.append(test_chars2)
            unknowns.pop(0)

        else:
            test_var = []
            for var in varieties:
                test_chars1 = []
                test_chars2 = []
                for v in var:
                    test_chars1.append(v)
                    test_chars2.append(v)

                test_chars1[unknowns[0]] = '.'
                test_var.append(test_chars1)
                test_chars2[unknowns[0]] = '#'
                test_var.append(test_chars2)

            unknowns.pop(0)
            varieties = test_var

        runs = runs + 1

    curr_result = 0
    for var in varieties:
        sets = []
        curr_set = 0
        for char in var:
            if char == "#":
                curr_set = curr_set + 1
            elif char == "." and curr_set != 0:
                sets.append(curr_set)
                curr_set = 0

        if curr_set != 0:
            sets.append(curr_set)

        if sets == nums:
            curr_result = curr_result + 1

    result = result + curr_result

print(f"result: {result}")