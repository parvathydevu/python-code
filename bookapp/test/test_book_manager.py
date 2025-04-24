import unittest
from book import Book
from book_manager import BookManager

class TestBookManager(unittest.TestCase):
    def setUp(self):
        self.manager = BookManager()
        self.book1 = Book("123", "Title1", "Author1", 2021)
        self.book2 = Book("456", "Title2", "Author2", 2022)
        self.manager.add_book(self.book1)
        self.manager.add_book(self.book2)

    def test_add_book(self):
        self.assertEqual(len(self.manager.view_books()), 2)

    def test_view_books(self):
        books = self.manager.view_books()
        self.assertIn(self.book1, books)
        self.assertIn(self.book2, books)

    def test_search_by_isbn(self):
        book = self.manager.search_by_isbn("123")
        self.assertEqual(book, self.book1)

    def test_delete_book(self):
        self.manager.delete_book("123")
        self.assertEqual(len(self.manager.view_books()), 1)
        self.assertNotIn(self.book1, self.manager.view_books())

if __name__ == "__main__":
    unittest.main()
