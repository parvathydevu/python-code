from book import Book

class BookManager:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def view_books(self):
        return self.books

    def search_by_isbn(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None

    def delete_book(self, isbn):
        self.books = [book for book in self.books if book.isbn != isbn]

