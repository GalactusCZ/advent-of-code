with open('day_4.txt') as f:
    cards = f.read()

# divide into cards
cards = cards.split('\n')

# go through cards
win = 0
for card in cards:
    # split into card parts
    card = card.split(': ')

    # split into numbers
    numbers = card[1].split(' | ')

    # get my numbers
    my_numbers_pre = numbers[0]
    my_numbers = []
    curr_num = 0
    for i in range(len(my_numbers_pre)):
        if my_numbers_pre[i].isdigit():
            curr_num = (curr_num * 10) + int(my_numbers_pre[i])

        if (my_numbers_pre[i] == ' ' and curr_num != 0) or i + 1 == len(my_numbers_pre):
            my_numbers.append(curr_num)
            curr_num = 0

    # get winning numbers
    win_numbers_pre = numbers[1]
    win_numbers = []
    curr_num = 0
    for i in range(len(win_numbers_pre)):
        if win_numbers_pre[i].isdigit():
            curr_num = (curr_num * 10) + int(win_numbers_pre[i])

        if (win_numbers_pre[i] == ' ' and curr_num != 0) or i + 1 == len(win_numbers_pre):
            win_numbers.append(curr_num)
            curr_num = 0

    print(my_numbers)
    print(win_numbers)
    # check if my numbers in winner numbers
    local_win = 0
    for my_number in my_numbers:
        if my_number in win_numbers:
            if local_win == 0:
                local_win = 1
            else:
                local_win = local_win * 2
    print(local_win)

    win = win + local_win

print(win)