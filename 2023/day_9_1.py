def get_nums(nums: list[int]) -> list[list[int]]:
    new_nums = []
    
    for i in range(len(nums)):
        if i == 0:
            continue
        
        new_nums.append(nums[i] - nums[i - 1])
        
    if new_nums.count(0) == len(new_nums):
        return None
        
    return_nums = get_nums(new_nums)
    
    if return_nums is not None:
        return_nums.append(new_nums)
        return return_nums
    else:
        return [new_nums]

with open('day_9.txt') as f:
    data = f.read()
    data = data.split('\n')
    
return_nums = []
for line in data:
    nums = line.split(' ')
    new_nums = []
    for num in nums:
        new_nums.append(int(num))
        
    return_nums = return_nums + get_nums(new_nums) + [new_nums]
    
calculated = 0
for num in return_nums:
    calculated = calculated + num[len(num) - 1]
    
print(calculated)