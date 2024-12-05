def order_updates(nums: list[int], rules: dict[int, list[int]]) -> int:
    new_odering: dict[int, list[int]] = {}
    present_nums = set(nums)

    for num in nums:
        if num in rules.keys():
            new_odering[num] = set()

            for x in rules[num]:
                if x in present_nums:
                    new_odering[num].add(x)

    predecessor_order: list[tuple[int, int]] = []

    for num in nums:
        amount = 0
        for pred in new_odering.values():
            if num in pred:
                amount += 1

        predecessor_order.append((amount, num))

    predecessor_order.sort()
    predecessor_order.reverse()

    for i, (_, num) in enumerate(predecessor_order):
        if i == len(predecessor_order) // 2:
            return num

    return 0


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
            retrieve = 0
            valid = True

            for i, num in enumerate(nums):
                if num in rules.keys():
                    for rule in rules[num]:
                        if rule in num_set and not rule in used_nums:
                            valid = False
                            retrieve = order_updates(nums, rules)
                            break

                used_nums.add(num)

            if not valid:
                result += retrieve

    print(result)
