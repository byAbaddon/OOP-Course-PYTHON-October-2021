class countdown_iterator:
    def __init__(self, num):
        self.num = num + 1

    def __iter__(self):
        return self   

    def __next__(self):
        if self.num:
            self.num -= 1
            return self.num
        raise StopIteration


'''
iterator = countdown_iterator(10)
for item in iterator:
    print(item, end=" ")
---------------
10 9 8 7 6 5 4 3 2 1 0 
'''