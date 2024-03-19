# read and split games 
with open('day_2.txt') as f:
    games = f.read()
    
games = games.split('\n')

num_sum = 0

# go through each game
for game in games:
    # split id and takes
    game = game.split(': ')
    
    max_rgb = [0, 0, 0]
    takes = game[1].split('; ')
    # all takes
    for take in takes:
        colors = take.split(', ')
        print(colors)
        
        # all colors
        for color in colors:
            print(color)
            data = color.split(' ')
            num = int(data[0])
            
            # red
            if data[1] == "red" and num > max_rgb[0]:
                max_rgb[0] = num
                
            # green 
            if data[1] == "green" and num > max_rgb[1]:
                max_rgb[1] = num
                
            # blue
            if data[1] == "blue" and num > max_rgb[2]:
                max_rgb[2] = num
            
    # adds num to sum
    new_num = 1
    for rgb in max_rgb:
        new_num = new_num * rgb
        
    print(game)
    print(max_rgb)
    print(new_num)
        
    num_sum = num_sum + new_num
        
print(num_sum)