class vowels:
    def __init__(self, words: str):
        self.words = words
        self.index = 0
        self.vowels_list = ['a', 'e', 'i', 'u', 'o', 'y']

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.words):
            current_index = self.index
            self.index += 1
            if self.words[current_index].lower() in self.vowels_list:
                return self.words[current_index]
            return self.__next__()
        raise StopIteration()

# my_string = vowels('Abcedifuty0o')
# for char in my_string:
#     print(char)
