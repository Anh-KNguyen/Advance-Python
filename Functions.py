# Functions are first class citizens in python
# functions can be assigned to variables and you can invoke a functin call on that variable
# can create new functions in real time, and you can return functions as a result value of a function as well

# executeBinaryFunction executes a function of type: F(x,y) -> z
def executeBinaryFunction(fn, arg0, arg1):
    return fn(arg0, arg1)

def addTwo(x, y) -> int:
    return x + y

func = addTwo
print(executeBinaryFunction(func, 5, 6))
print(executeBinaryFunction(addTwo, 1, 2))  # can also just pass in addTwo directly


# printerFactory returns a function that you can call later, which prints a message
def printerFactory(message):
    # define helper function
    def printer():
        print(message)
    return printer

myPrinter = printerFactory('hi')
myPrinter()

myPrinter2 = printerFactory('hi2')
myPrinter2()

myPrinter()

