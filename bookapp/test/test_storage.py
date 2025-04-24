import unittest
import os
from book import Book
from storage import Storage

class TestStorage(unittest.TestCase):
    def setUp(self):
        self.filepath = 'test_books.json'
        self.storage = Storage()

    def test_save_load(self):
        book_list = [
            Book("123", "Title1", "Author1", 2021),
            Book("456", "Title2", "Author2", 2022),
            Book("789", "Title3", "Author3", 2023),
            Book("012", "Title4", "Author4", 2024)
        ]

        self.storage.save_to_file(book_list, self.filepath)
        loaded_books = self.storage.load_from_file(self.filepath)
        self.assertEqual(len(loaded_books), 4)
        self.assertEqual(loaded_books[0].isbn, "123")
        self.assertEqual(loaded_books[1].title, "Title2")
        self.assertEqual(loaded_books[2].author, "Author3")
        self.assertEqual(loaded_books[3].publication_year, 2024)

    def tearDown(self):
        if os.path.exists(self.filepath):
            os.remove(self.filepath)

if __name__ == "__main__":
    unittest.main()
