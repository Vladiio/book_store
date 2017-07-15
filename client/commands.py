import sys

from store import views


def display_books():
    books = views.book_view()
    for book in books:
        print(book)
    

def quit():
    print("Buy buy")
    raise sys.exit(1)
