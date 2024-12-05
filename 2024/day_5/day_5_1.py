with open("day_5.txt") as f:
    rules: dict[int, list[int]] = {}
    writing_rules = True
    result = 0

    for line in f:
        line = line.replace('\n', '')

        if line == '':
            writing_rules = False

        elif writing_rules:
            line = line.split('|')
            
            if int(line[1]) not in rules.keys():
                rules[int(line[1])] = [int(line[0])]

            else:
                rules[int(line[1])].append(int(line[0]))

        else:
            line = line.split(',')
            nums = [int(x) for x in line]
            num_set = set(nums)
            used_nums: set[int] = set()
            mid_num = 0
            valid = True

            for i, num in enumerate(nums):
                if num in rules.keys():
                    for rule in rules[num]:
                        if rule in num_set and not rule in used_nums:
                            valid = False
                            break

                if i == len(nums) // 2:
                    mid_num = num

                used_nums.add(num)

            if valid:
                result += mid_num

    print(result)
