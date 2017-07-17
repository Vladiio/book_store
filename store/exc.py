

class StoreException(Exception):
    
    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)


class CategoryDoesNotExist(StoreException):
    pass


class BookDoesNotExist(StoreException):
    pass


class CategoryAlreadyExist(StoreException):
    pass


class BookAlreadyExist(StoreException):
    pass
