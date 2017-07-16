import sys

from store.views import main_view
from store.models import Category, Book
from store import exc
from client.utils import get_int, get_string, \
        get_book_info
from database.conf import session


def display_categories(request):
    cat_name = get_string("Enter category name please",
                          default="all")
    print("\tID\tNAME\tBOOKS")
    if cat_name == "all":
        cats = main_view.get_category_list()
        for cat in cats:
            print(cat)
    else:
        cat = main_view.get_category(cat_name)
        print(cat)


def display_books(request):
    cat_id = get_int("Enter category id please")
    print("\tID\tTITLE\tAUTHOR\tPRICE") 
    books = main_view.get_book_list(cat_id)
    for book in books:
         print(book)


def add_book(request):
    book_info = get_book_info()
    try:
        main_view.create_book(*book_info)
    except exc.ObjectDoesNotExist as err:
        print(f"Error: category {err.name} does not exist")
    else:
        request.changes = True
        print("Book created")


def quit(request):
    if request.changes:
        if input("Save changes?(y/n): ") == "y":
            session.commit()
            print("Saved")
    print("Buy buy")
    raise sys.exit(1)

