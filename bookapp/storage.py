import json
from book import Book

class Storage:
    @staticmethod
    def save_to_file(books, filename):
        with open(filename, 'w') as file:
            json_books = [book.__dict__ for book in books]
            json.dump(json_books, file)

    @staticmethod
    def load_from_file(filename):
        try:
            with open(filename, 'r') as file:
                json_books = json.load(file)
                return [Book(**book) for book in json_books]
        except FileNotFoundError:
            return []
