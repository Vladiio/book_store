from abc import ABCMeta, abstractmethod

from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound 

from store.models import Book, Category
from store import exc
from database.conf import session



class BaseView(metaclass=ABCMeta):

    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.objects().all()

    @abstractmethod
    def get(self, title):
        pass        

    @abstractmethod
    def create(self):
        pass
    

class CategoryView(BaseView):

    def __init__(self):
        super().__init__(Category)
        
    def get(self, title):
        try:
            category =  self.model.objects().filter(
                             self.model.name==title).one()
        except NoResultFound:
            raise exc.CategoryDoesNotExist(title)
        else:
            return category
        
    def create(self, cat_name):
        cat = self.model(name=cat_name)
        try:
            cat.save()
        except IntegrityError:
            raise exc.CategoryAlreadyExist(cat_name)


category_view = CategoryView()


class BookView(BaseView):

    def __init__(self):
        super().__init__(Book)

    def get(self, title):
        try:
            book = self.model.objects().filter(
                        self.model.title==title).one()
        except NoResultFound:
            raise exc.BookDoesNotExist(title)
        else:
            return book

    def fetch(self, cat_id):
        return self.model.objects().filter(
                    self.model.category_id==cat_id).all()

    def create(self, cat_name, 
               title, author, price):
        try:
            category = category_view.get(cat_name)
        except IntegrityError:
            raise exc.BookAlreadyExist(title)
        else:
            book = Book(title=title, author=author,
                        category_id=category.id, price=price)
            book.save()


book_view = BookView()

