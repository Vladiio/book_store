from category import Category
from book import Book, BookDoesNotExist


class Menu:
    def __init__(self):
        self.commands = {
            "": None
        }



book1 = Book("oop", "dusty", 23)
book2 = Book("django", "Two scops", 54)
cat = Category("Programming")

for book in (book1, book2):
    cat.add_book(book)


cat.display_books()
try:
    book = cat.find_by_title("oop1")
except BookDoesNotExist as err:
    print("The book '{}' does not exist".format(err.title))
