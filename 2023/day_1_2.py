with open('day_1.txt') as f:
    words = f.read()
    
words2 = words.split('\n')

spell_num = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

number = 0
for word in words2:
    inner_numbers = []
    blank_letters = ""
    
    for i in range(len(word)):
        if word[i].isdigit():
            inner_numbers.append(int(word[i]))
            
        else:
            blank_letters = blank_letters + word[i]
            
            for sn in spell_num:
                if sn in blank_letters:
                    inner_numbers.append(spell_num.index(sn) + 1)
                    
                    blank_letters = ""
                    
                    break
                    
        if len(inner_numbers) == 1:
            print(inner_numbers)
            break
            
    word2 = word[::-1]
    blank_letters = ""
    for i in range(len(word2)):
        if word2[i].isdigit():
            inner_numbers.append(int(word2[i]))
            
        else:
            blank_letters =  word2[i] + blank_letters
            
            for sn in spell_num:
                if sn in blank_letters:
                    inner_numbers.append(spell_num.index(sn) + 1)
                    
                    blank_letters = ""
                    
                    break
                    
        if len(inner_numbers) == 2:
            break
                    
    print(f"Word: {word}, in: {inner_numbers}")
    if len(inner_numbers) > 0:
        new_number = (inner_numbers[0] * 10) + inner_numbers[len(inner_numbers) - 1]
        print(new_number)
        number = number + new_number
        
print(number)