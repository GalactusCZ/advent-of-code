with open("./1_day.txt") as f:
    dial = 50
    zeros = 0

    for line in f:
        line = line.replace("\n", "")
        num = int(line[1::])
        if line[0] == 'R':
            dial = (dial + num) % 100
        else:
            dial = (dial - num) % 100

        if dial == 0:
            zeros += 1

    print(zeros)