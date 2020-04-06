class List:
    def reverse() -> None: # modifies in place, doesn't return anything
        pass


a_list = ['3','2','1'] # could be tuple..etc
a_tuple = (3, 2, 1)
def reversed(iterable): # returns a copy of iterable
    lst = list(iterable)
    lst.reverse()

    # return lst

    # convert to generator
    for i in lst:
        yield i


print(list(reversed(a_list)))
print(tuple(reversed(a_tuple)))