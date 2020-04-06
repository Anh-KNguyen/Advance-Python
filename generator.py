lst = [2, 3, 4]

def generator(iterable):
    yield iterable[0]
    yield iterable[1]
    yield iterable[2]

x = generator(lst)

print(x.__next__())
print(x.__next__())
print(x.__next__())
