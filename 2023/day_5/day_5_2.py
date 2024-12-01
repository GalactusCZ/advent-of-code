with open('day_5.txt') as f:
    data = f.read()
    data = data.split('\n')

# gets seeds
seeds_separation = data[0].split(': ')
seeds_str = seeds_separation[1].split(' ')
seed_ranges = []
first = True
for s in seeds_str:
    if first:
        trans_val = int(s)
        first = False
    else:
        first = True
        seed_ranges.append([trans_val, trans_val + int(s)])

# goes through line
sts = stf = ftw = wtl = ltt = tth = htl = False
stsl = []
stfl = []
ftwl = []
wtll = []
lttl = []
tthl = []
htll = []
for line in data:
    str_transfer = []
    int_transfer = []
    # reset vars if line is empty
    if line == '':
        sts = stf = ftw = wtl = ltt = tth = htl = False

    # seed-to-soil
    if sts:
        str_transfer = line.split(' ')
        int_transfer = [int(str_transfer[0]), int(str_transfer[1]), int(str_transfer[2])]
        stsl.append(int_transfer)

    # soil-to-fertilizer
    if stf:
        str_transfer = line.split(' ')
        int_transfer = [int(str_transfer[0]), int(str_transfer[1]), int(str_transfer[2])]
        stfl.append(int_transfer)

    # fertilizer-to-water
    if ftw:
        str_transfer = line.split(' ')
        int_transfer = [int(str_transfer[0]), int(str_transfer[1]), int(str_transfer[2])]
        ftwl.append(int_transfer)

    # water-to-light
    if wtl:
        str_transfer = line.split(' ')
        int_transfer = [int(str_transfer[0]), int(str_transfer[1]), int(str_transfer[2])]
        wtll.append(int_transfer)

    # light-to-temperature
    if ltt:
        str_transfer = line.split(' ')
        int_transfer = [int(str_transfer[0]), int(str_transfer[1]), int(str_transfer[2])]
        lttl.append(int_transfer)

    # temperature-to-humidity
    if tth:
        str_transfer = line.split(' ')
        int_transfer = [int(str_transfer[0]), int(str_transfer[1]), int(str_transfer[2])]
        tthl.append(int_transfer)

    # humidity-to-location
    if htl:
        str_transfer = line.split(' ')
        int_transfer = [int(str_transfer[0]), int(str_transfer[1]), int(str_transfer[2])]
        htll.append(int_transfer)

    # seed-to-soil
    if 'seed-to-soil' in line:
        sts = True

    # soil-to-fertilizer
    if 'soil-to-fertilizer' in line:
        stf = True

    # fertilizer-to-water
    if 'fertilizer-to-water' in line:
        ftw = True

    # water-to-light
    if 'water-to-light' in line:
        wtl = True

    # light-to-temperature
    if 'light-to-temperature' in line:
        ltt = True

    # temperature-to-humidity
    if 'temperature-to-humidity' in line:
        tth = True

    # humidity-to-location
    if 'humidity-to-location' in line:
        htl = True

# translates values
a = 1
i = 63170000
final_loc = None
while final_loc is None:
    print(i)
    # humidity-to-location
    location = i
    humidity = location
    for rang in htll:
        if location >= rang[0] and location < (rang[0] + rang[2]):
            offset = 0
            offset = location - rang[0]
            humidity = rang[1] + offset

            break

    # temperature-to-humidity
    temperature = humidity
    for rang in tthl:
        if humidity >= rang[0] and humidity < (rang[0] + rang[2]):
            offset = 0
            offset = humidity - rang[0]
            temperature = rang[1] + offset

            break

    # light-to-temperature
    light = temperature
    for rang in lttl:
        if temperature >= rang[0] and temperature < (rang[0] + rang[2]):
            offset = 0
            offset = temperature - rang[0]
            light = rang[1] + offset

            break

    # water-to-light
    water = light
    for rang in wtll:
        if light >= rang[0] and light < (rang[0] + rang[2]):
            offset = 0
            offset = light - rang[0]
            water = rang[1] + offset

            break

    # fertilizer-to-water
    fertilizer = water
    for rang in ftwl:
        if water >= rang[0] and water < (rang[0] + rang[2]):
            offset = 0
            offset = water - rang[0]
            fertilizer = rang[1] + offset

            break

    # soil-to-fertilizer
    soil = fertilizer
    for rang in stfl:
        if fertilizer >= rang[0] and fertilizer < (rang[0] + rang[2]):
            offset = 0
            offset = fertilizer - rang[0]
            soil = rang[1] + offset

            break

    # seed-to-soil
    seed = soil
    for rang in stsl:
        if soil >= rang[0] and soil < (rang[0] + rang[2]):
            offset = 0
            offset = soil - rang[0]
            seed = rang[1] + offset

            break

    for ran in seed_ranges:
        if seed in range(ran[0],ran[1]):
            final_loc = location
            print(f"final seed: {seed}")
            break

    i = i + a

print(final_loc)