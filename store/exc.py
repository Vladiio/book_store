

class StoreException(Exception):
    pass


class ObjectDoesNotExist(StoreException):
    
    def __init__(self, name, *args, **kwargs):
        self.name = name
        super().__init__(*args, **kwargs)

