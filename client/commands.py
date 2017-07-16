import sys

from store.views import main_view
from store.models import Category, Book
from client.utils import get_int, get_string


def display_categories():
    cat_name = get_string("Enter category name please",
                          default="all")
    cats = main_view.get_categories(cat_name)
    print("\tID\tNAME\tBOOKS")
    for cat in cats:
        print(cat)


def display_books():
    cat_id = get_int("Enter category id please",
                      default=0)
    books = main_view.get_books(cat_id)
    print("\tID\tTITLE\tAUTHOR\tPRICE") 
    for book in books:
        print(book)


def quit():
    print("Buy buy")
    raise sys.exit(1)

