with open('day_3.txt') as f:
    engine = f.read()
    
engine = engine.split('\n')
    
# finds special chars
spec = []
for x in range(len(engine)):
    for y in range(len(engine[x])):
        if engine[x][y] != '.' and not engine[x][y].isdigit():
            spec.append([x,y])
            
# finds numbers
valid_num = 0
full_num = 0
is_valid = False
for x in range(len(engine)):
    for y in range(len(engine[x])):
        # checks if digit
        if not engine[x][y].isdigit():
            continue
            
        full_num = (10 * full_num) + int(engine[x][y])
        
        # checks for special chars
        if is_valid == False and ([x - 1, y + 1] in spec or [x, y + 1] in spec or [x + 1, y + 1] in spec or [x + 1, y] in spec or [x + 1, y - 1] in spec or [x, y - 1] in spec or [x - 1, y - 1] in spec or [x - 1, y] in spec):
            is_valid = True
            
        # checks next part
        if y + 1 >= len(engine[x]) or not engine[x][y + 1].isdigit():
            if is_valid:
                valid_num = valid_num + full_num
            
            full_num = 0
            is_valid = False 
            
print(valid_num)