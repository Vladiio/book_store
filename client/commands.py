import sys

from store.views import category_view, book_view
from store.models import Category, Book
from store import exc
from client.utils import get_int, get_string, \
        get_book_info
from database.conf import session


def display_categories(request):
    cat_name = get_string("Enter category name please",
                          default="all")
    if cat_name == "all":
        print("\tID\tNAME\tBOOKS")
        cats = category_view.get_all()
        for cat in cats:
            print(cat)
    else:
        cat = category_view.get(cat_name)
        print(cat)


def display_books(request):
    cat_id = get_int("Enter category id please")
    books = category_view.get(cat_id)
    print("\tID\tTITLE\tAUTHOR\tPRICE") 
    for book in books:
         print(book)


def add_book(request):
    book_info = get_book_info()
    try:
        book_view.create(*book_info)
    except exc.CategoryDoesNotExist as err:
        print(f"Error: category {err.name} does not exist")
    else:
        request.changes = True
        print("Book created")


def add_category(request):
    cat_name = get_string("Enter category name")
    try:
        category_view.create(cat_name)
    except exc.CategoryAlreadyExist as err:
        print(f"Error: category {err.name} exists")
    else:
        print("Category created")


def quit(request):
    if request.changes:
        if input("Save changes?(y/n): ") == "y":
            session.commit()
            print("Saved")
    print("Buy buy")
    raise sys.exit(1)

