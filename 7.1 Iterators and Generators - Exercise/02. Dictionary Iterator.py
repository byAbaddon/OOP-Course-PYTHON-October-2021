class dictionary_iter:
    def __init__(self, obj: dict):
        self.obj = obj

    def __iter__(self):
        return self

    def __next__(self):
        for k, v in self.obj.items():
            current = (k, v)
            del self.obj[k]
            return current
        raise StopIteration


'''
result = dictionary_iter({1: "1", 2: "2"})
for x in result:
    print(x)
-----------------
(1, '1')
(2, '2')
'''