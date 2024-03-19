def hashmap(code: str) -> int:
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

    # Prints result
    return curr_res

def box_insert(boxes: dict, ins: str) -> dict:
    c_split = ins.split('=')
    lense = c_split[0]
    foc_len = int(c_split[1])
    insertion = lense + ' ' + str(foc_len)
    box = hashmap(lense)
    
    if box in boxes.keys():
        contents = boxes[box]
       
        is_in = False
        for i in range(len(contents)):
            check_s = contents[i].split(' ')
            
            if lense == check_s[0]:
                is_in = True
                contents[i] = insertion
                break
                
        if is_in == False:
            contents.append(insertion)
            
        boxes[box] = contents
        
    else:
        boxes[box] = [insertion]

    return boxes

def boxes_rem(boxes: dict, rem: str) -> dict:
    rem = rem[:len(rem)-1]
    box = hashmap(rem)

    # If box exists
    if box in boxes.keys():
        contents = boxes[box]

        # If value exists
        for i in range(len(contents)):
            c_split = contents[i].split(' ')
            
            if rem == c_split[0]:
                contents.pop(i)
                break

        boxes[box] = contents

    return boxes

with open('day_15.txt') as f:
    data = f.read()
    data = data.split(',')

result = 0
boxes = {}

# Goes through codes
for code in data:
    # If "="
    if '=' in code:
        boxes = box_insert(boxes, code)

    # If "-"
    elif '-' in code:
        boxes = boxes_rem(boxes, code)

# Goes through keys
for j in range(256):
    contents = []

    if j in boxes.keys():
        contents = boxes[j]
    
    if contents == []:
        print(j)
        continue

    # Goes through items in box
    for i in range(len(contents)):
        # Splits items
        c_split = contents[i].split(' ')
        foc_len = int(c_split[1]) # Gets focal length

        # Calculates current result
        curr_res = (j + 1) * (i + 1) * foc_len
        #print(f"{j + 1} * {i + 1} * {foc_len}")
        print(f"{j}. {c_split[0]} = {curr_res}")
        result += curr_res

print(boxes)
print(result)