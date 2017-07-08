def calculateHandlen(hand):
    counter = 0

    for letter in hand:
        counter += hand.get(letter, 0)
    return counter

print(calculateHandlen({'a': 1, 'b': 1, 'c': 0}))