# range(start, stop, step)

# range is not a generator
# it is "lazy" since it doesn't generate every number that it "contains" when we create it
# instead it gives those numbers as we need them when looping over it
# ON NEED BASIS

def range(start, stop):
    while start < stop:
        yield start
        start += 1

for i in range(5, 10):
    print(i)


