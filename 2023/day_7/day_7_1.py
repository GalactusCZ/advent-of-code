with open('day_7.txt') as f:
    data = f.read()
    data = data.split('\n')

# Split cards and bids
cards = []
bids = []
for line in data:
    set = line.split(' ')
    cards.append(set[0])
    bids.append(int(set[1]))

# Get numeric version of cards
possible_values = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
num_cards = []
sorted_num_cards = []
for card in cards:
    this_card = []
    for char in card:
        this_card.append(possible_values.index(char))

    num_cards.append(this_card)
    sorted_num_cards.append(this_card)

# Sort numeric cards
sorted_num_cards.sort()

# Turns sorted numeric cards to normal
sorted_cards = []
for snc in sorted_num_cards:
    sorted_cards.append(cards[num_cards.index(snc)])

fik, fok, fuh, thk, twp, onp, hic = [], [], [], [], [], [], []
for card in sorted_cards:
    used_values = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    for char in card:
        used_index = possible_values.index(char)
        used_values[used_index] = used_values[used_index] + 1

    if 5 in used_values:
        fik.append(cards.index(card))

    elif 4 in used_values:
        fok.append(cards.index(card))

    elif 3 in used_values and 2 in used_values:
        fuh.append(cards.index(card))

    elif 3 in used_values:
        thk.append(cards.index(card))

    elif used_values.count(2) == 2:
        twp.append(cards.index(card))

    elif 2 in used_values:
        onp.append(cards.index(card))

    else:
        hic.append(cards.index(card))

managed_cards = hic + onp + twp + thk + fuh + fok + fik

result = 0
for i in range(len(managed_cards)):
    result = result + bids[managed_cards[i]] * (i + 1)

print(result)