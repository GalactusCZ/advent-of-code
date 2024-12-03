with open("day_3.txt") as f:
    result = 0
    active = True
    for line in f:
        mul_c = 0
        linec = ''
        do_c = 0
        open_mul = False
        open_do = False
        do_nt = False
        first = True
        nums: list[str] = ['', '']
        
        for char in line:
            linec += char
            if char == 'm':
                do_c = 0
                open_do = False
                mul_c = 1
                
            elif char == 'u' and mul_c == 1:
                mul_c += 1
                
            elif char == 'l' and mul_c == 2:
                mul_c += 1
            
            elif char == 'd':
                mul_c = 0
                open_mul = False
                do_c = 1
                
            elif char == 'o' and do_c == 1:
                do_c += 1
                
            elif char == 'n' and do_c == 2:
                do_c += 1
                
            elif char == '\'' and do_c == 3:
                do_c += 1
                
            elif char == 't' and do_c == 4:
                do_c += 1
                
            elif char == '(' and ((mul_c == 3 and not open_mul) or ((do_c == 2 or do_c == 5) and not open_do)):
                if mul_c == 3:
                    open_mul = True
                    first = True
                    nums = ['', '']
                    
                elif do_c == 2:
                    open_do = True
                    do_nt = True
                    
                else:
                    open_do = True
                    do_nt = False
                
            elif char.isdecimal() and open_mul:
                if first:
                    nums[0] += char
                    
                else:
                    nums[1] += char
                    
            elif char == ',' and open_mul and first:
                first = False
            
            elif char == ')' and ((open_mul and not first) or open_do):
                if open_mul and active:
                    result += int(nums[0]) * int(nums[1])
                elif open_do:
                    print(linec)
                    linec = ''
                    active = do_nt

                mul_c = 0
                do_c = 0
                first = True
                open_mul = False
                open_do = False
            
            else:
                mul_c = 0
                do_c = 0
                first = True
                open_mul = False
                open_do = False

        #     print(active, char)

        # print(linec)

    print(result)