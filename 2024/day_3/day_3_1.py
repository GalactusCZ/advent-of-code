with open("day_3.txt") as f:
    result = 0
    for line in f:
        mul_c = 0
        open_mul = False
        first = True
        nums: list[str] = ['', '']
        
        for char in line:
            if char == 'm' and mul_c == 0:
                mul_c += 1
                
            elif char == 'u' and mul_c == 1:
                mul_c += 1
                
            elif char == 'l' and mul_c == 2:
                mul_c += 1
                
            elif char == '(' and mul_c == 3 and not open_mul:
                open_mul = True
                first = True
                nums = ['', '']
                
            elif char.isdecimal() and open_mul:
                if first:
                    nums[0] += char
                    
                else:
                    nums[1] += char
                    
            elif char == ',' and open_mul and first:
                first = False
            
            elif char == ')' and open_mul and not first:
                mul_c = 0
                first = True
                open_mul = False
                
                result += int(nums[0]) * int(nums[1])
            
            else:
                mul_c = 0
                first = True
                open_mul = False
            
    print(result)