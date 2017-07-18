import sys

from store.views import category_view, book_view
from store.models import Category, Book
from store import exc
from client.utils import get_int, get_string, \
        get_book_info
from database.conf import session


class Commander:
    
    def __init__(self):
        self.book_header = "\tID\tNAME\tBOOKS"
        self.cat_header = "\tID\tTITLE\tAUTHOR\tPRICE"
        self.saved = True

    def display_category_list(self):
        cats = category_view.get_all()
        print(self.book_header)
        for cat in cats:
            print(cat)

    def display_book_list(self):
        cat_id = get_int("Enter category id please")
        books = book_view.get_all(cat_id)
        print(self.cat_header) 
        for book in books:
            print(book)

    def display_category(self):
        cat_title = get_string("Enter category title please") 
        try:
            cat = category_view.get(cat_title)
        except exc.ObjectDoesNotExist as err:
            print(f"There is no category {err.name}")
        else:
            print(self.book_header)
            print(cat)
        

    def display_book(self):
        book_title = get_string("Enter book title please")
        try:
            book = book_view.get(book_title)
        except exc.ObjectDoesNotExist as err:
            print(f"Error: book {err.name} does not exist")
        else:
            print(book)

    def add_category(self):
        cat_name = get_string("Enter category name")
        try:
            category_view.create(title=cat_name)
        except exc.ObjectAlreadyExist as err:
            print(f"Error: category {err.name} exists")
        else:
            print("Category created")
    
    def add_book(self):
        book_info = get_book_info()
        try:
            book_view.create(**book_info)
        except exc.ObjectAlreadyExist as err:
            print(f"Error: category {err.name} does not exist")
        else:
            self.saved = False
            print("Book created")

    def quit(self):
        print("Buy buy")
        raise sys.exit(1)


commander = Commander()
