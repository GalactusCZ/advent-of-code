with open('day_2.txt') as f:
    data = f.read()
    data = data.split('\n')
    
score = 0
for line in data:
    play = line.split(' ')
    
    if play[1] == 'X':
        score = score + 0
        
        if play[0] == 'A':
            score = score + 3
        if play[0] == 'B':
            score = score + 1
        if play[0] == 'C':
            score = score + 2

    if play[1] == 'Y':
        score = score + 3
        
        if play[0] == 'A':
            score = score + 1
        if play[0] == 'B':
            score = score + 2
        if play[0] == 'C':
            score = score + 3

    if play[1] == 'Z':
        score = score + 6
        
        if play[0] == 'A':
            score = score + 2
        if play[0] == 'B':
            score = score + 3
        if play[0] == 'C':
            score = score + 1

print(score)