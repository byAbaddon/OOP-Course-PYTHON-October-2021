def even_numbers(fun):
    def wrapper(numbers):
        return [x for x in numbers if not x & 1]
    return wrapper


'''
@even_numbers
def get_numbers(numbers):
    return numbers
print(get_numbers([1, 2, 3, 4, 5]))
--------------------
[2, 4]
'''