def multiply(n):
    def decorator(fun):
        def wrapper(number):
            return fun(number) * n
        return wrapper
    return decorator


'''
@multiply(3)
def add_ten(number):
    return number + 10

print(add_ten(3))

---------------
39
'''


