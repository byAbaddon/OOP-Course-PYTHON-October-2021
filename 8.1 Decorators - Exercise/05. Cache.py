def cache(fun):
    def wrapper(args):
        result = fun(args)
        wrapper.log[args] = result
        return result
    wrapper.log = {}
    return wrapper


'''
@cache
def fibonacci(n):
    if n < 2:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)

fibonacci(4)
print(fibonacci.log)

----------------------
{1: 1, 0: 0, 2: 1, 3: 2}
'''