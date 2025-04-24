class Book:
    def __init__(self, isbn, title, author, publication_year):
        self.isbn = isbn
        self.title = title
        self.author = author
        self.publication_year = publication_year

    def __repr__(self):
        return f"Book(ISBN={self.isbn}, Title={self.title}, Author={self.author}, Year={self.publication_year})"

