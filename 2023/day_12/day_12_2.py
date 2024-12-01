import time
start_time = time.time()

def get_results(chars: str, nums: list[int]) -> int:
    # Ends recursion if there are no more nums
    if nums == []:
        # Returns valid or invalid
        if '#' in chars:
            return 0
        else:
            return 1

    # Local variables
    curr_nums = nums
    curr_chars = chars
    curr_result = 0
    curr_cache = {}

    # Min length
    min_length = 0
    for num in curr_nums:
        min_length = min_length + num + 1

    min_length = min_length - 1
    #print(min_length)

    """
    # Variations if there is section with just "?"
    if curr_chars[0] == "?":
        j = 0
        while len(curr_chars) > j and curr_chars[j] == "?":
            j = j + 1

        if j > curr_nums[0]:
            print(j)
    """

    # Variations
    j = 0
    while len(curr_chars[j:]) >= min_length:
        section = curr_chars[j:j + curr_nums[0]]

        # Checks if section can be used
        if '.' not in section and '#' not in curr_chars[:j] and curr_chars[j + curr_nums[0]:j + curr_nums[0] + 1] != "#":
            given_chars = curr_chars[j + curr_nums[0] + 1:]
            given_nums = curr_nums[1:]
            # Recursion
            gotten_result = get_results(given_chars, given_nums)
            curr_result += gotten_result
            #print(curr_chars[j + curr_nums[0] + 1:])
            #print(curr_nums[1:])

        j = j + 1

    return curr_result

with open('day_12_test.txt') as f:
    data = f.read()
    data = data.split('\n')

result = 0
ln = 0
for line in data:
    ln = ln + 1
    print("------------------------------")
    print(ln)
    line = line.split(' ')

    # Set up numbers
    nums = line[1].split(',')
    nums = [int(x) for x in nums]

    # Set up chars
    chars = line[0]

    new_chars,new_nums = '',[]
    for i in range(5):
        new_chars = new_chars + chars + '?'
        new_nums.extend(nums)

    new_chars = new_chars[:len(new_chars) - 1]

    chars = new_chars
    nums = new_nums

    # Shortens spaces
    while '..' in chars:
        chars = chars.replace('..', '.')

    # Removes end space
    if chars[len(chars) - 1] == '.':
        chars = chars[:len(chars) - 1]

    # Removes begining space
    if chars[0] == '.':
        chars = chars[1:]

    """
    while True:
        cont = True
        last_num = nums[len(nums) - 1]
        reverse_chars = chars[::-1]

        if reverse_chars[0] == '#':
            cont = False
            reverse_chars = reverse_chars[last_num + 1:]
            nums.pop()

        chars = reverse_chars[::-1]

        if chars[0] == '#':
            cont = False
            chars = chars[nums[0]:]
            nums.pop(0)

        if cont:
            break
    """

    curr_result = get_results(chars, nums)
    print(curr_result)

    result = result + curr_result
    print(result)

print(f"result: {result}")
print("Process finished --- %s seconds ---" % (time.time() - start_time))