with open('day_1.txt') as f:
    data = f.read()
    data = data.split('\n')
    
calories = []
curr_cal = 0
for line in data:
    if line == '':
        calories.append(curr_cal)
        curr_cal = 0
        
    else:
        curr_cal = curr_cal + int(line)

calories.append(curr_cal)
        
print(max(calories))