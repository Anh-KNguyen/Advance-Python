# When you execute some function and want that function to call you back after you don't do something
# Pass what is called a "callback" function to it

import time

# no callback
def doSomething(doneMessage: str):
    time.sleep(2)
    print(doneMessage)


# callback
def doSomethingCB(cb=None):
    time.sleep(2)
    if cb is not None:
        cb()        # call the callback

def finishedCallback():
    print('we finished')
    print('yay')

doSomethingCB(finishedCallback)