class Integer:
    def __init__(self, value: int):
        self.value = value

    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            return cls(round(value))
        return "value is not a float"

    @classmethod
    def from_roman(cls, value):
        roman = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        result = 0
        for i in range(len(value) - 1, -1, -1):
            num = roman[value[i]]
            if 3 * num < result:
                result -= num
            else:
                result += num
        return cls(result)

    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            return cls(int(value))
        return "wrong type"


first_num = Integer(10)
print(first_num.value)

second_num = Integer.from_roman("IV")
print(second_num.value)

print(Integer.from_float("2.6"))
print(Integer.from_string(2.6))


'''
10
4
value is not a float
wrong type
'''