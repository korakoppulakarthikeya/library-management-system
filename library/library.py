import logging
from .storage import Storage
from .book import Book

class Library:

    def __init__(self):
        self.books = Storage.load_books()

    def add_book(self, book_id, title, author):
        book = Book(book_id, title, author)
        self.books.append(book)
        Storage.save_books(self.books)
        logging.info(f"Book added: {title}")

    def remove_book(self, book_id):
        self.books = [b for b in self.books if b.book_id != book_id]
        Storage.save_books(self.books)
        logging.info(f"Book removed: {book_id}")

    def issue_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id and book.available:
                book.available = False
                Storage.save_books(self.books)
                logging.info(f"Book issued: {book.title}")
                return True
        return False

    def return_book(self, book_id):
        for book in self.books:
            if book.book_id == book_id:
                book.available = True
                Storage.save_books(self.books)
                logging.info(f"Book returned: {book.title}")
                return True
        return False

    def view_books(self):
        return self.books