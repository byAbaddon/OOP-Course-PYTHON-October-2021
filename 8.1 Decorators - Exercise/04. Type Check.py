def type_check(type_of):
    def decorator(fun):
        def wrapper(arg):
            if type_of == type(arg):
                return fun(arg)
            return 'Bad Type'
        return wrapper
    return decorator


'''
@type_check(int)
def times2(num):
    return num*2
print(times2(2))
print(times2('Not A Number'))
-------------------------
4
Bad Type
'''