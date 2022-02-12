def solution():
    def integers():
        for n in range(1, 10_000_000):
            yield n

    def halves():
        for x in integers():
            yield x / 2

    def take(n, seq):
        arr = []
        for i in seq:
            if len(arr) != n:
                arr.append(i)
            else:
                return arr

    return take, halves, integers


'''
take = solution()[0]
halves = solution()[1]
print(take(5, halves()))
-----------------------------
[0.5, 1.0, 1.5, 2.0, 2.5]
'''