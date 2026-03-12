import json
import os
from .book import Book

DATA_FILE = "data/books.json"

class Storage:

    @staticmethod
    def load_books():
        if not os.path.exists(DATA_FILE):
            return []

        with open(DATA_FILE, "r") as file:
            data = json.load(file)
            return [Book.from_dict(book) for book in data]

    @staticmethod
    def save_books(books):
        with open(DATA_FILE, "w") as file:

            json.dump([book.to_dict() for book in books], file, indent=4)