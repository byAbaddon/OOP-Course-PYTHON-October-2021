def genrange(s, e):
    while not s == e + 1:
        yield s
        s += 1


'''
print(list(genrange(1, 10)))
-------------
[1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
'''















