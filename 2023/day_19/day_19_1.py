with open('day_19_test.txt') as f:
    data = f.read().split('\n')
    
# Base variables
next = False
paths = {}
origins  = []

# Goes through lines
for line in data:
    # If line is empty, switch to origins
    if line == '':
        next = True
        continue
    
    # Get origins
    if next:
        line = line[1:len(line) - 1].split(',')
        
        curr_orig = {}
        # Gets parameters of origins
        for part in line:
            part = part.split('=')
            
            curr_orig[part[0]] = int(part[1])
            
        origins.append(curr_orig)
        
    # Else appends paths
    else:
        line = line.split('{')
        line[1] = line[1][:len(line[1]) - 1]
        
        index = line[0]
        vals = line[1].split(',')
        
        paths[index] = vals
        
print(paths)
print(origins)
result= 0

# Goes through origins
for o in origins:
    # Base var
    i = 'in'
    
    # Runs the pathfinding process
    while True:
        # Gets operations
        operations = paths[i]
        further = ''
        
        # Goes through operations
        for op in operations:
            # If operation has logic
            if ':' in op:
                op = op.split(':')
                val = int(op[0][2:])
                
                # Proceeds with logic calculationd
                if (op[0][1] == '<' and o[op[0][0]] < val) or (op[0][1] == '>' and o[op[0][0]] > val):
                    further = op[1]
                    break
                    
                else:
                    continue
                    
            # Else it is used as value
            else:
                further = op
                break
                
        # Accepted
        if further == 'A':
            result += o['x'] + o['m'] + o['a'] + o['s']
            break
        # Rejected
        elif further == 'R':
            break
        # Continuation
        else:
            i = further
            
print(result)