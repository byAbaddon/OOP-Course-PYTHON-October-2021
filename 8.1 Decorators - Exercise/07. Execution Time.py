from timeit import default_timer as timer


def exec_time(fun):
    def wrapper(*args, **kwargs):
        start_time = timer()
        fun(*args, **kwargs)
        stop_time = timer()

        return stop_time - start_time

    return wrapper


'''
@exec_time
def loop(start, end):
    total = 0
    for x in range(start, end):
        total += x
    return total
print(loop(1, 10000000))
------------------------------Time will be different for every CPU  

0.8481780600013735
'''

