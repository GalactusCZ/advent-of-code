import re

with open('day_6.txt') as f:
    data = f.read()
    data = data.split('\n')

time = int(re.sub('(Time:)(\s)+|\s+', '', data[0]))
distance = int(re.sub('(Distance:)(\s)+|\s+', '', data[1]))

half_time = time / 2

change = 1
i = half_time + 13700000
ms = 13700000
while True:
    traveled_distance = i * (time - i)

    if traveled_distance > distance:
        ms = ms + 1
    else:
        break
    print(f"first: {ms}")

    i = i + change

ms = ms + 13700000
change = -1
i = half_time - 13700001
while True:
    traveled_distance = i * (time - i)

    if traveled_distance > distance:
        ms = ms + 1
    else:
        break
    print(f"second: {ms}")

    i = i + change

print(ms)