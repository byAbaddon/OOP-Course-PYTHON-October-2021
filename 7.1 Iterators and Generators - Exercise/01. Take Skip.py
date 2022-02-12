class take_skip:
    def __init__(self, step: int, count: int):
        self.step = step
        self.count = count
        self.result = -1

    def __iter__(self):
        return self

    def __next__(self):
        if self.result >= self.count - 1:
            raise StopIteration
        self.result += 1
        return self.result * self.step


'''
numbers = take_skip(2, 6)
for number in numbers:
    print(number)
-------------
0
2
4
6
8
10
'''


