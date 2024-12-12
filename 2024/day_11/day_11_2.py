elel = {0: [['1'], ['2024'], ['20', '24'], ['2', '0', '2', '4']], 1: [['2024'], ['20', '24'], ['2', '0', '2', '4']], 2: [['4048'], ['40', '48'], ['4', '0', '4', '8']], 3: [['6072'], ['60', '72'], ['6', '0', '7', '2']], 4: [['8096'], ['80', '86'], ['8', '0', '8', '6']], 5: [['10120'], ['20482880'], ['2048', '2880'], ['20', '48', '28', '80'], ['2', '0', '4', '8', '2', '8', '8', '0']], 6: [['12144'], ['24579456'], ['2457', '9456'], ['24', '57', '94', '56'], ['2', '4', '5', '7', '9', '4', '5', '6']], 7: [['14168'], ['28576032'], ['2857', '6032'], ['28', '57', '60', '32'], ['2', '8', '5', '7', '6', '0', '3', '2']], 8: [['16192'], ['32772608'], ['3277', '2608'], ['32', '77', '26', '8']], 9: [['18216'], ['36869184'], ['3686', '9184'], ['36', '86', '91', '84'], ['3', '6', '8', '6', '9', '1', '8', '4']], 125: [['253000'], ['253', '0']], 253: [['512072'], ['512', '72']], 512: [['1036288'], ['2097446912'], ['4245232549888'], ['8592350680973312'], ['85923506', '80973312'], ['8592', '3506', '8097', '3312'], ['85', '92', '35', '6', '80', '97', '33', '12']]}

def split(num: str, elel: dict[int, list[list[str]]], amount: int) -> int:
    print(amount)
    result = 0

    if len(num) == 2:
        if num[0] == num[1]:
            result += split(num[0], elel, amount - 1) * 2

        else:
            result += split(num[0], elel, amount - 1) + split(num[1], elel, amount - 1)

    elif len(elel[int(num)]) >= amount:
        return len(elel[int(num)][amount - 1])

    else:
        local_rem = {}

        for var in elel[int(num)][-1]:
            if var in local_rem.keys():
                result += local_rem[var]

            else:
                retrieve = split(var, elel, amount - len(elel[int(num)]))
                local_rem[var] = retrieve
                result += retrieve

    return result

with open("day_11.txt") as f:
    line = f.readline().replace('\n', '').split(' ')

    result = 0

    for num in line:
        result += split(num, elel, 25)

    print(result)