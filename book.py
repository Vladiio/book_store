

class BookException(Exception):
    
    def __init__(self, id=None, title=None):
        super().__init__(id, title)
        self.id = id
        self.title = title


class BookDoesNotExist(BookException):
    pass


class BookAlreadyExist(BookException):
    pass



class Book:
    _count = 0

    def __init__(self, title,
                 author, price):
        Book._count += 1
        self.id = Book._count
        self.title = title
        self.author = author
        self._price = price

    def __str__(self):
        return "{0.id}, {0.title}, " \
               "{0.author}, {0.price}".format(self)
    
    @property
    def price(self):
        return self._price

    @price.setter
    def price(self, new_price):
        self._price = float(new_price)
