from itertools import permutations


def possible_permutations(arr):
    for x in permutations(arr):
        yield list(x)

'''
[print(n) for n in possible_permutations([1, 2, 3])]
-----------
[1, 2, 3]
[1, 3, 2]
[2, 1, 3]
[2, 3, 1]
[3, 1, 2]
[3, 2, 1]
'''