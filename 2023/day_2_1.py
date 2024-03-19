# read and split games 
with open('day_2.txt') as f:
    games = f.read()
    
games = games.split('\n')

max_rgb = [12, 13, 14]
id_sum = 0

# go through each game
for game in games:
    # split id and takes
    game = game.split(': ')
    
    fits = True
    takes = game[1].split('; ')
    # all takes
    for take in takes:
        colors = take.split(', ')
        
        # all colors
        for color in colors:
            data = color.split(' ')
            
            # red
            if data[1] == "red" and int(data[0]) > max_rgb[0]:
                fits = False
                break
                
            # green 
            if data[1] == "green" and int(data[0]) > max_rgb[1]:
                fits = False
                break
                
            # blue
            if data[1] == "blue" and int(data[0]) > max_rgb[2]:
                fits = False
                break
                
        if fits == False:
            break
            
    # adds id to sum
    if fits == True:
        id = game[0].split(' ')
        
        id_sum = id_sum + int(id[1])
        
print(id_sum)