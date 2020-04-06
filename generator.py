lst = [2, 3, 4]

def generator(iterable):
    for i in iterable:
        yield i

x = generator(lst)

# next(x) equivalent to x.__next__()

# print(x.__next__())
# print(x.__next__())
# print(x.__next__())

# generator objects are iterable
for item in generator(lst):
    print(item)