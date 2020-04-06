# same output = [(0, 'a'), (1, 'b'), (2, 'c')]

# returns enumerate object (tuples -immutable list)
# each pair = (idx, value)

letters = ['a', 'b', 'c']
listOfLetters = []

n = 0

for letter in letters:
    listOfLetters.append((n, letter))
    n += 1

print(listOfLetters)

# letters = ['a', 'b', 'c']
# print(list(enumerate(letters)))