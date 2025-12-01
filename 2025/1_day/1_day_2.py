with open("./1_day.txt") as f:
    dial = 50
    zeros = 0

    for line in f:
        curr_dial = dial
        line = line.replace("\n", "")
        num = int(line[1::])

        zeros += num // 100
        num %= 100

        if line[0] == 'R':
            dial += num
        else:
            dial -= num

        if dial <= 0 or dial >= 100:
            if curr_dial != 0:
                zeros += 1
            if dial < 0:
                dial += 100
            if dial >= 100:
                dial -= 100

    print(zeros)