def even_parameters(fun):
    def wrapper(*args):
        get_even = [x for x in args if isinstance(x, int) and not x & 1]
        if len(get_even) == len(args):
            return fun(*args)
        return 'Please use only even numbers!'
    return wrapper


'''
@even_parameters
def add(a, b):
    return a + b

print(add(2, 4))
print(add( "Peter", 1))

--------------------------
6
Please use only even numbers!
'''