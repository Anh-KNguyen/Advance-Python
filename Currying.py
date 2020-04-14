# Concept from functional programming
# currying arguements is where you return a function that takes another parameter
# rather than having multiple parameters in one function
# currying in a way, lazily evaluates parameters of a function

def add(x):
    def adder(y):
        return x + y
    return adder        # returns the "adder" function with x bound to a value

sum = add(1)(2)     # sum = (add(1)) (2)
print(sum)

partialSum = add(1) 
finalSum = partialSum(4)    # finish it off = 1
print(finalSum)


def foo(x, y, z):
    pass

def fooCurry(x):
    def inner(y):
        def inner2(z):
            return x + y + z
        return inner2
    return inner

print(fooCurry(1)(2)(3))


# executeBinaryFunctionCurry (fn: x -> y -> int, int, int) -> int
# fn must be a binary function, which means it must be of the form:
# fn: x -> y -> int
def executeBinaryFunctionCurry(fn, arg1, arg2):
    return fn(arg1)(arg2)

print(executeBinaryFunctionCurry(add, 4, 5))


# F(x: int, y: int, z: int) -> int
# Proper curry definition form:
# threeSum x -> y -> z -> int
def threeSum(x):
    def inner1(y):
        def inner2(z):
            return x + y + z
        return inner2
    return inner1

print(threeSum(1)(2)(3))


# threeSum x -> y -> z -> int
partialSum = threeSum(5)    # partialSum is a two parameter curry function F(y, z) -> int (because x was bound to 5)
# partialSum: threeSum(5): y -> z -> int
# when we call it with one function, there is only y and z function calls left to call
# partialSum: y -> z -> int

print(executeBinaryFunctionCurry(partialSum, 6, 7))


# Note: for currying, partial() exists to "freeze" some portion of a function's arguments
# resulting in a new object