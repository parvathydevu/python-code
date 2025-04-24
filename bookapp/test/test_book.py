import unittest
from book import Book

class TestBook(unittest.TestCase):
    def setUp(self):
        self.book = Book("123", "Title1", "Author1", 2021)

    def test_book_attributes(self):
        self.assertEqual(self.book.isbn, "123")
        self.assertEqual(self.book.title, "Title1")
        self.assertEqual(self.book.author, "Author1")
        self.assertEqual(self.book.publication_year, 2021)

    def test_book_representation(self):
        self.assertEqual(repr(self.book), "Book(ISBN=123, Title=Title1, Author=Author1, Year=2021)")

if __name__ == "__main__":
    unittest.main()
