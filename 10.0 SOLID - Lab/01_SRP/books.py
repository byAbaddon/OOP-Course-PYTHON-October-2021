class Library:
    def __init__(self, location):
        self.location = location
        self.books = []
        
    
    def add_book_to_library(self, book):
        if book not in self.books:
            self.books.append(book)

    def find_book(self, title):
        try:
            is_book = [x for x in self.books if x.title == title][0]
            return f'We have the book - {is_book.title} from Library in {self.location}'
        except:
            return 'Book not found!'


class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author   
        self.page = 0

    def turn_page(self, page):
        self.page = page
        return  f'You open page № {self.page}'




b = Book('AliBaba', 'Bojkov')
l = Library('Dubay')
l.add_book_to_library(b)
print(l.find_book('AliReza'))
print(l.find_book('AliBaba'))
print(b.turn_page(22))



   