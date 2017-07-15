"""
The module contains a Category class.
"""


from book_store import book


class Category:
    """Represent category of books.
    
    """
    
    def __init__(self, name):
        self.name = name
        self.items = {}

    def display_books(self):
        """Print all books in the category."""
        for item in self.items.values():
            print(item)
    
    def add_book(self, item):
        """Add book to the category."""
        if isinstance(item, book.Book):
            if item.id not in self.items:
                self.items[item.id] = item
            else:
                raise book.BookAlreadyExist(id=item.id)

    def find_by_title(self, title):
        """Return a book with specified title."""
        for item in self.items.values():
            if item.title == title:
                return item
        else:
            raise book.BookDoesNotExist(title=title)
    
    def find_by_id(self, id):
        try:
            item = self.items[id] 
        except KeyError:
            raise book.BookDoesNotExist(id=id)
        else:
            return item

