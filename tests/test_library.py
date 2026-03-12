import pytest
from library.library import Library

def test_add_book():
    lib = Library()
    lib.add_book(99, "Test Book", "Tester")

    books = lib.view_books()
    assert any(book.book_id == 99 for book in books)

def test_issue_book():
    lib = Library()
    lib.add_book(100, "Issue Test", "Tester")
    result = lib.issue_book(100)
    assert result == True