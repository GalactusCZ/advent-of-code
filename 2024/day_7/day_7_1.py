def try_calc(suma: int, curr_suma: int, numbers: list[int]) -> bool:
    if len(numbers) == 1:
        # print(suma, curr_suma + numbers[0], (curr_suma * numbers[0]))
        return suma == (curr_suma + numbers[0]) or suma == (curr_suma * numbers[0])

    return try_calc(suma, curr_suma + numbers[0], numbers[1:]) or \
           try_calc(suma, curr_suma * numbers[0], numbers[1:])

with open("day_7.txt") as f:
    calculations: list[tuple[int, list[int]]] = []

    for line in f:
        line = line.split(": ")
        calculations.append((int(line[0]), [int(x) for x in line[1].split(" ")]))

    print(calculations)
    result = 0

    for nums in calculations:
        key, numbers = nums
        if try_calc(key, 0, numbers):
            result += key

    print(result)
