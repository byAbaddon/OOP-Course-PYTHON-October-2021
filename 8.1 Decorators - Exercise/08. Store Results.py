class store_results:
    def __init__(self, fun):
        self.fun = fun

    def __call__(self, *args):
        with open('results.txt', 'a') as file:
            file.write(f'Function \'{self.fun.__name__}\' was add called. Result: {self.fun(*args)}\n')


@store_results
def add(a, b):
    return a + b

@store_results
def mult(a, b):
    return a * b

add(2, 2)
mult(6, 4)