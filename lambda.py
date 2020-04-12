# Does function in-line
# Drawback of lambda: only one line
import time

# callback
def doSomethingCB(cb=None):
    time.sleep(2)
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