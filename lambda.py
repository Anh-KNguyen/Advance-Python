# Does function in-line
# Drawback of lambda: only one line
import time

# callback
def doSomethingCB(cb=None):
    time.sleep(1)
    if cb is not None:
        cb()        # call the callback

def finishedCallback():
    print('we finished')
    print('yay')

# lambda lets you define a function as an expression
finishedLambda = lambda: print('we finished (lambda version - define a function as an expression)')   # can't have two print statements


doSomethingCB(finishedCallback)
doSomethingCB(finishedLambda)
doSomethingCB(lambda : print('we finished (lambda version)'))



def doMoreWork(cb=None):
    time.sleep(1)
    if cb is not None:
        msg = cb()
        print(msg)

def callback() -> str:
    print('callback called')
    return 'hello'


doMoreWork(callback)
doMoreWork()        # if cb not given, it defaults to None


doMoreWork(finishedLambda)
# msg = cb()		# will print we finished lamba version - define a function as an expression
# print(msg)		# then none since lamba is one line



# lambda : <expression body here>
# translation to
# def function():
# 	return <expression body here>



# Callbacks with parameters
def doLongWork(cb=None):
    time.sleep(1)
    x = "long work took 1 second"
    if cb is not None:
        msg = cb(x)
        print(msg)

def callbackLongWork(x: str) -> str:
    return 'we finished ' + x

doLongWork(callbackLongWork)

# to do this in lambda
cbLongWorkLambda = lambda x: 'we finished (lambda version)' + x

def cbLongWorkLambdaExpanded(x: str, y: str) -> str:
    return 'we finished (lambda version) ' + x + y

doLongWork(cbLongWorkLambda)