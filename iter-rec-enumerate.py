from typing import *

def iterativeEnumerate(items: List[str]) -> List[Tuple[int, str]]:
    out = []
    count = 0
    for item in items:
        tup = (count, item)
        out += [tup]
        count += 1
    return out


def recursiveEnumerate(items: List[str]) -> List[Tuple[int, str]]:
    def helper(count: int, lst: list):
        if lst is None or len(lst) == 0:
            return []

        head = lst[0]
        tail = lst[1:]

        tup = (count, head)

        return [tup] + helper(count+1, tail)
        


    return helper(0, items) 
        


testcases = [
    ["hello", "there", "love"],
    ['a', 'b', 'c', 'd']
]

for tc in testcases:
    assert list(enumerate(tc)) == list(iterativeEnumerate(tc))
    assert list(enumerate(tc)) == list(recursiveEnumerate(tc))
