import sys
from book import Book
from book_manager import BookManager
from storage import Storage

def main():
    manager = BookManager()
    manager.books = Storage.load_from_file('books.json')

    while True:
        print("\nLibrary Management System")
        print("1. Add a book")
        print("2. View all books")
        print("3. Search for a book by ISBN")
        print("4. Delete a book")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            isbn = input("Enter ISBN: ")
            title = input("Enter title: ")
            author = input("Enter author: ")
            year = input("Enter publication year: ")
            book = Book(isbn, title, author, year)
            manager.add_book(book)
            Storage.save_to_file(manager.view_books(), 'books.json')
            print("Book added successfully!")

        elif choice == '2':
            books = manager.view_books()
            for book in books:
                print(book)

        elif choice == '3':
            isbn = input("Enter ISBN to search: ")
            book = manager.search_by_isbn(isbn)
            if book:
                print(book)
            else:
                print("Book not found.")

        elif choice == '4':
            isbn = input("Enter ISBN to delete: ")
            manager.delete_book(isbn)
            Storage.save_to_file(manager.view_books(), 'books.json')
            print("Book deleted successfully!")

        elif choice == '5':
            print("Exiting...")
            sys.exit()

        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
