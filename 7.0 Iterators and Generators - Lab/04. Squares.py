def squares(n, result=0):
    while result < n:
        result += 1
        yield result ** 2


'''
print(list(squares(5)))
---------------
[1, 4, 9, 16, 25]
'''
