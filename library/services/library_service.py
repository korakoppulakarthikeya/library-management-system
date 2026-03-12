from library.models.book import Book
from library.models.user import User

class LibraryService:
    def __init__(self):
        self.books = []
        self.users = []

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)
        print("Book added successfully")

    def register_user(self, user_id, name):
        user = User(user_id, name)
        self.users.append(user)
        print("User registered successfully")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and not book.is_issued:
                book.is_issued = True
                print("Book issued successfully")
                return
        print("Book not available")

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.is_issued:
                book.is_issued = False
                print("Book returned successfully")
                return
        print("Invalid return request")

    def show_books(self):
        for book in self.books:
            print(book)
