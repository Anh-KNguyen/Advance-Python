# Advance-Python

Generators

    list - executes immediately
  
    generators - function that returns iterable (generator) objects by calling yield (primative operator).
  
    Calling next() on a generator iterable resumes the execution from where yield was called (not at the beginning of the fuunction)

sort() and sorted()

    sort() - changes on hard copy. in-place sorting
    
    sorted() - returns a copy because an interable is passed in. You cannot "change" an iterable
    
enumerate()

    enumerate() - returns enumerate object (tuples - immutable objects)
    
    Each pair = (idx, value). Under the hood is a for loop appending to a list.
