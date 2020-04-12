# Advance-Python

Generators

    list - executes immediately
  
    generators - function that returns iterable (generator) objects by calling yield (primative operator)
  
    Calling next() on a generator iterable resumes the execution from where yield was called (not at the beginning of the fuunction)

Functional Programming - Annonymous Functions

    Mutating variables is not allowed. Function doesn't store or modify any variable. It only takes inputs and returns outputs.

    Allows you to pass in the same thing and get the same answer rather than an addition to the original answer.

Callbacks

    Callback function will execute once/if the first function completes.

Lambda

    Does function in-line. Only one line.
    
    Lambda lets you define a function as an expression and can also be passed into a function.

sort() and sorted()

    sort() - changes on hard copy. in-place sorting
    
    sorted() - returns a copy because an interable is passed in. You cannot "change" an iterable
    
reverse() and reversed()

    reverse() - modifies in-place, doesn't return anything
    
    reversed() - returns a copy of iterable
    
enumerate()

    enumerate() - returns enumerate object (tuples - immutable objects)
    
    Each pair = (idx, value). Under the hood is a for loop appending to a list
    
range()

    range is not an iterator. It is "lazy" since it generate numbers as we need them
    
    Range objects are like sequences (lists, tuples, strings). They contain no memory under the hood
