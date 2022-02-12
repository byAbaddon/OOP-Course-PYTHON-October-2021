def read_next(*args):
    for prop in args:
        for el in prop:
            yield str(el)


'''
for item in read_next('string', (2,), {'d': 1, 'i': 2, 'c': 3, 't': 4}):
    print(item, end='')
--------------------------
string2dict
'''
