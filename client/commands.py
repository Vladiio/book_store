import sys

from store.views import main_view
from store.models import Category, Book
from client.utils import get_int


def display_categories():
    cats = main_view.get_all()
    print("ID\tNAME\tBOOKS")
    for cat in cats:
        print(cat)


def display_books():
    cat_id = get_int("Enter category id please: ")
    books = main_view.get_books(cat_id)
    for book in books:
        print(book)


def quit():
    print("Buy buy")
    raise sys.exit(1)

