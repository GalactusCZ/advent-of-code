def try_calc(suma: int, curr_suma: int, numbers: list[int]) -> bool:
    if len(numbers) == 1:
        return suma == (curr_suma + int(numbers[0])) or \
               suma == (curr_suma * int(numbers[0])) or \
               suma == (int(str(curr_suma) + numbers[0]))

    return try_calc(suma, curr_suma + int(numbers[0]), numbers[1:]) or \
           try_calc(suma, curr_suma * int(numbers[0]), numbers[1:]) or \
           try_calc(suma, int(str(curr_suma) + numbers[0]), numbers[1:])


def num_len(num: int) -> int:
    length = 0

    while num > 0:
        num //= 10
        length += 1

    return length


with open("day_7.txt") as f:
    calculations: list[tuple[int, list[int]]] = []

    for line in f:
        line = line.replace("\n", "")
        line = line.split(": ")
        calculations.append((int(line[0]), line[1].split(" ")))

    result = 0

    for nums in calculations:
        key, numbers = nums
        if try_calc(key, 0, numbers):
            result += key

    print(result)
