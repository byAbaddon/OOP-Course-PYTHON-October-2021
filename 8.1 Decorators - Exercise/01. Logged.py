def logged(fun):
    def wrapper(*args):
        return f'you called {fun.__name__}{args}\nit returned {fun(*args)}'
    return wrapper


'''
@logged
def func(*args):
    return 3 + len(args)
print(func(4, 4, 4))
---------------------
you called func(4, 4, 4)
it returned 6
'''