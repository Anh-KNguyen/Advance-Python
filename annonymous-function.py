from typing import List

# In functional programming, you don't mutate variables

def sum(lst: List[int]) -> int:
    s = 0
    for x in lst:
        s += x      # this isn't allowed in functional programming because s is being mutated by incrementing it

    return s

# Functional = function that doesn't store/modify any variable. It only takes inputs and returns an output
# aka "pure function"

def functionalSum(lst: List[int]) -> int:
    
    def helperSumFunc(lst: List[int], counter:int) -> int:
        if len(lst) == 0 or lst == None: return counter
        head, tail = lst[0], lst[1:]    # split lst into single element, and array containing everything else
        # head = 1, tail [2,3,4]
        return helperSumFunc(tail, counter + head)
    
    return helperSumFunc(lst, 0)

print(functionalSum([1,2,3,4]))



# If you pass in the same function, you'll get different answers
# Functional Programming allows you to pass in the same thing and get the same answer

# non-pure function
globalSum = [0]

def foobar(x: int):
    globalSum[0] += x
    return globalSum

print(foobar(2))        # prints [2]
print(foobar(2))        # prints [4]
