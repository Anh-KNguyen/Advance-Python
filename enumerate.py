# same output = [(0, 'a'), (1, 'b'), (2, 'c')]

# returns enumerate object (tuples -immutable list)
# each pair = (idx, value)

def enumeratee(iterable):
    i = 0
    for item in iterable:
        yield i, item
        i += 1

lst = ['a', 'b', 'c']

print(list(enumerate(lst)))

# letters = ['a', 'b', 'c']
# print(list(enumerate(letters)))