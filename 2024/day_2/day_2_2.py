safe = 0

with open("day_2.txt") as file:
    for main_line in file:
        main_line = main_line.split(" ")

        for i in range(len(main_line)):
            line = [int(x) for j, x in enumerate(main_line) if j != i]

            is_safe = True
            rise_dec_set = False
            rising = True
            prev_level = int(line.pop())

            while len(line) > 0:
                this_level = int(line.pop())

                if not rise_dec_set:
                    if not (0 < abs(this_level - prev_level) < 4):
                        is_safe = False
                        break

                    if this_level < prev_level:
                        rising = False

                    rise_dec_set = True

                else:
                    if (not (0 < abs(this_level - prev_level) < 4)) or \
                    (rising and this_level < prev_level) or \
                    (not rising and this_level > prev_level):
                        is_safe = False
                        break

                prev_level = this_level

            if is_safe:
                safe += 1
                break

print(safe)
