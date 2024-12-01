with open('day_15.txt') as f:
    data = f.read()
    data = data.split(',')
    
result = 0

# Goes through codes
for code in data:
    curr_res = 0
    
    # Goes through chars
    for char in code:
        # To ASCII
        asc = ord(char)
            
        # Add to current result
        curr_res += asc
            
        # Multiplies
        curr_res = curr_res * 17
            
        # Gets remainder
        curr_res = (curr_res % 256)
            
    # Adds to result
    result += curr_res
    
print(result)