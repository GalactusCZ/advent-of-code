def splt(num: str, amount: int, cache: dict[tuple[str, int], list[str]]) -> int:
    if (num, amount) in cache.keys():
        return cache[(num, amount)]
    else:
        if num == '0':
            curr_nums = ['1']

        elif len(num) % 2 == 0:
            curr_nums = [num[:len(num) // 2], num[len(num) // 2:]]

            for i in range(2):
                while curr_nums[i][0] == '0' and len(curr_nums[i]) > 1:
                    curr_nums[i] = curr_nums[i][1:]

        else:
            curr_nums = [str(2024 * int(num))]


    if amount - 1 == 0:
        cache[(num, amount)] = len(curr_nums)
        return len(curr_nums)

    result = 0

    for c_num in curr_nums:
        result += splt(c_num, amount - 1, cache)

    cache[(num, amount)] = result

    return result


with open("day_11.txt") as f:
    line = f.readline().replace('\n', '').split(' ')

    cache: dict[tuple[str, int], list[str]] = {}
    result = 0
    i = 1

    for st in line:
        result += splt(st, 75, cache)
        print(f"{i}/{len(line)}")
        i += 1

    print(result)