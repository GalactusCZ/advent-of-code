with open('day_1.txt') as f:
    words = f.read()
    
words2 = words.split('\n')

number = 0
for word in words2:
    inner_numbers = []
    
    for i in range(len(word)):
        if word[i].isdigit():
            inner_numbers.append(int(word[i]))
            
    if len(inner_numbers) > 0:
        new_number = (inner_numbers[0] * 10) + inner_numbers[len(inner_numbers) - 1]
        
        number = number + new_number
        
print(number)