from functools import reduce

class Calculator:

    @staticmethod
    def add(*args):
        return sum(list(args))

    @staticmethod
    def multiply(*args):
        return reduce(lambda a, x: a * x, args) 

    @staticmethod
    def divide(*args):
        return reduce(lambda a, x: a / x, args) 

    @staticmethod
    def subtract(*args):
        return reduce(lambda a, x: a - x, args)

