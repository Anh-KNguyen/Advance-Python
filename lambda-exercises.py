import functools

helloLambda = lambda : "hello world"

def helloLambdaFunc():
    return "hello world"




def addOne(x: int) -> int:
    x += 1
    return x


addOneLambda = lambda x : x + 1

assert list(map(addOne, [1,2,3,4])) == list(map(addOneLambda, [1,2,3,4]))
