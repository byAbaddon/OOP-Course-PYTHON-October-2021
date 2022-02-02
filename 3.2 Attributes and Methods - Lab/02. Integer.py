class Integer:
    def __init__(self, value):
        self.value = value
    
    @classmethod
    def from_float(cls, value):
        if isinstance(value, float):
            return Integer(int(value))
        return 'value is not a float'
        

    @classmethod
    def from_roman(cls, num):
        roman_numerals = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        result = 0
        for i, c in enumerate(num):
            if (i + 1) == len(num) or roman_numerals[c] >= roman_numerals[num[i + 1]]:
                result += roman_numerals[c]
            else:
                result -= roman_numerals[c]
        return Integer(result)


    @classmethod
    def from_string(cls, value):
        if isinstance(value, str):
            return Integer(int(value))  
        return 'wrong type'

      
    def add(self, integer): #Integer
        if not isinstance(integer, Integer):
            return f'number should be an Integer instance'
        return self.value + integer.value 

    def __str__(self):
        return f'{self.value}'
