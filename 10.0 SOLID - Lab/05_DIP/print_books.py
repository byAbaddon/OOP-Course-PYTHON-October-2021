class Book:
    def __init__(self, content: str):
        self.content = content


class Formatter:
    def format(self, book: Book):
        return book.content

class Printer:
    def get_book(self, book: Book, formater):
        formatter = Formatter()
        formatted_book = formatter.format(book)
        return formatted_book


b = Book('content') 
f = Formatter()
f.format(b) 
p = Printer()
print(p.get_book(b, 'f'))
    