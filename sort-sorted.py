# sorts items in place
# changes hard copy
class List:
    def sort(key=None, reverse=False) -> None:
        # do quicksort with key, reverse if reverse == True
        pass

a_list = ['2','1','3']
def sorted(iterable):
    lst = list(iterable)
    lst.sort() # modifes lst in place

    # return lst

    # convert to generator object, can be converted to list
    for i in lst:
        yield i

# returns a copy
# sorts iterable passed in
# you cannot "change" an iterable

# sorted(iterable, *, key=None, reverse=False)
print(list(sorted(a_list)))