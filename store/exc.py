

class StoreException(Exception):
    
    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)


class ObjectDoesNotExist(StoreException):
    pass


class ObjectAlreadyExist(StoreException):
    pass

