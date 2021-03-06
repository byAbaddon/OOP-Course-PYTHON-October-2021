def vowel_filter(fun):
    def wrapper():
        vowels = ['a', 'e', 'o', 'u', 'i', 'y']
        return [x for x in fun() if x in vowels]
    return wrapper


'''
@vowel_filter
def get_letters():
    return ["a", "b", "c", "d", "e"]


print(get_letters())
-------------------------
["a", "e"]
'''