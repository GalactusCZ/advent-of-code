with open('day_20.txt') as f:
    data = f.read().split('\n')

# Name: Type | Goal | Memory | State
modules = {}
for line in data:
    # Splits into originator and goal
    line = line.split(' -> ')

    # Gets goals
    if ',' in line[1]:
        goals = line[1].split(', ')
    else:
        goals = [line[1]]


    # Broadcaster
    if line[0] == 'broadcaster':
        modules['broadcaster'] = ['broadcaster', goals, None, None]

    # Button
    elif line[0] == 'button':
        modules['button'] = ['button', goals, None, None]

    # Flip-flop
    elif line[0][0] == '%':
        name = line[0][1:]

        modules[name] = ['%', goals, [], 'off']

    # Conjunction
    elif line[0][0] == '&':
        name = line[0][1:]

        modules[name] = ['&', goals, [], None]

print(modules)
high, low = 0,0

# Button presses
for i in range(1000):
    #print("-----------------------")
    curr_high,curr_low = 0,0

    # Creates original query according to existence of button
    if 'button' in modules.keys():
        query_row = [['button', 'low']]
    else:
        query_row = [['broadcaster', 'low']]

    # Goes through the query row
    while query_row != []:
        #print(query_row[0])
        name = query_row[0][0]
        pulse = query_row[0][1]
        query_row.pop(0)


        if name != 'button':
            # Counts high and low pulses
            if pulse == 'high':
                curr_high += 1
            else:
                curr_low += 1

        if name == 'output' or name == "rx":
            continue

        module = modules[name]

        # Broadcaster
        if module[0] == 'broadcaster':

            for goal in module[1]:
                query_row.append([goal, pulse])

        # Button
        elif module[0] == 'button':

            for goal in module[1]:
                query_row.append([goal, pulse])

        # Flip-flop
        elif module[0] == '%':
            # Activates only when recieving low pulse
            if pulse == 'low':
                new_pulse = ''

                # Flips from 'off' to 'on'
                if module[3] == 'off':
                    module[3] = 'on'
                    new_pulse = 'high'

                # Flips from 'on' to 'off'
                else:
                    module[3] = 'off'
                    new_pulse = 'low'

                # Updates module
                modules[name] = module

                # Adds queries
                for goal in module[1]:
                    query_row.append([goal, new_pulse])

        # Conujunction
        elif module[0] == '&':
            # Counts or flips connected to this conjunction
            flips = []
            for key in modules.keys():
                # Gets flip-flop value
                if modules[key][0] == '%' and name in modules[key][1]:
                    flips.append(modules[key][3])

                # Gets conjunction value
                elif modules[key][0] == '&' and name in modules[key][1]:
                    memory = modules[key][2]

                    if memory == [] or memory == 'high':
                        flips.append('on')
                    else:
                        flips.append('off')


            # Calculates new pulse
            new_pulse = ''
            if flips.count('on') == len(flips):
                new_pulse = 'low'
            else:
                new_pulse = 'high'

            # Memory
            module[2] = new_pulse
            modules[name] = module

            # Adds queries
            for goal in module[1]:
                query_row.append([goal, new_pulse])

    #print(modules)
    high += curr_high
    low += curr_low
    #print(f"curr high: {curr_high}, low: {curr_low}")

print(f"high: {high}, low: {low}")
print(f"multiplication: {high * low}")