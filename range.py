# range(start, stop, step)

# range is not a generator
# it is "lazy" since it doesn't generate every number that it "contains" when we create it
# instead it gives those numbers as we need them when looping over it
# ON NEED BASIS

for i in range(5):
    pass

for i in [0,1,2,3,4]:
    pass

iterable = [0,1,2,3,4]
for i in range(iterable):
    pass