with open('day_5.txt') as f:
    data = f.read()
    data = data.split('\n')
    
# gets seeds
seeds_separation = data[0].split(': ')
seeds_str = seeds_separation[1].split(' ')
seeds = []
for s in seeds_str:
    seeds.append(int(s))

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
    print('"' + line + '"')
    # reset vars if line is empty
    if line == '':
        sts = stf = ftw = wtl = ltt = tth = htl = False
        print(sts)
    
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
locations = []
for seed in seeds:
    # seed-to-soil
    soil = seed
    for rang in stsl:
        if seed >= rang[1] and seed < (rang[1] + rang[2]):
            offset = 0
            offset = seed - rang[1]
            soil = rang[0] + offset
            
            break
            
    # soil-to-fertilizer
    fertilizer = soil
    for rang in stfl:
        if soil >= rang[1] and soil < (rang[1] + rang[2]):
            offset = 0
            offset = soil - rang[1]
            fertilizer = rang[0] + offset
            
            break
            
    # fertilizer-to-water
    water = fertilizer
    for rang in ftwl:
        if fertilizer >= rang[1] and fertilizer < (rang[1] + rang[2]):
            offset = 0
            offset = fertilizer - rang[1]
            water = rang[0] + offset
            
            break
    
    # water-to-light
    light = water
    for rang in wtll:
        if water >= rang[1] and water < (rang[1] + rang[2]):
            offset = 0
            offset = water - rang[1]
            light = rang[0] + offset
            
            break
    
    # light-to-temperature
    temperature = light
    for rang in lttl:
        if light >= rang[1] and light < (rang[1] + rang[2]):
            offset = 0
            offset = light - rang[1]
            temperature = rang[0] + offset
            
            break
    
    # temperature-to-humidity
    humidity = temperature
    for rang in tthl:
        if temperature >= rang[1] and temperature < (rang[1] + rang[2]):
            offset = 0
            offset = temperature - rang[1]
            humidity = rang[0] + offset
            
            break
    
    # humidity-to-location 
    location = humidity
    for rang in htll:
        if humidity >= rang[1] and humidity < (rang[1] + rang[2]):
            offset = 0
            offset = humidity - rang[1]
            location = rang[0] + offset
            
            break
    
    locations.append(location)

print(min(locations))