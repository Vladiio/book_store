from store.models import Book
from database.conf import session


def book_view():
    books = session.query(Book).all()
    return books


def add_book_view(title, author, price):
    book = Book(title=title,
                author=author,
                price=price)
    book.save()
