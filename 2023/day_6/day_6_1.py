import re

with open('day_6.txt') as f:
    data = f.read()
    data = data.split('\n')

old_time = re.split('\s+', re.sub('(\s)+', ' ', re.sub('(Time:)(\s)+', '', data[0])))
old_distance = re.split('\s+', re.sub('(\s)+', ' ', re.sub('(Distance:)(\s)+', '', data[1])))

# to number conversion
time = []
distance = []
for i in range(len(old_time)):
    time.append(int(old_time[i]))
    distance.append(int(old_distance[i]))

# goes through races
result = 1
for i in range(len(time)):
    valid_tries = 0
    # goes through tries
    for hold in range(time[i]):
        traveled_distance = hold * (time[i] - hold)

        if traveled_distance > distance[i]:
            valid_tries = valid_tries + 1

    if valid_tries != 0:
        result = result * valid_tries

print(result)