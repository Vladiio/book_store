from sqlalchemy.exc import IntegrityError
from sqlalchemy.orm.exc import NoResultFound 

from store.models import Book, Category
from store import exc
from store.settings import session


class BaseView:

    def __init__(self, model):
        self.model = model

    def get_all(self):
        return self.model.objects().all()

    def get(self, title):
        try:
            obj =  self.model.objects().filter(
                        self.model.title==title).one()
        except NoResultFound:
            raise exc.ObjectDoesNotExist(title)
        else:
            return obj
    
    def create(self, **kwargs):
        try:
            obj = self.model(**kwargs)
            obj.save()
        except IntegrityError:
            raise exc.ObjectAlreadyExist(kwargs.get("title"))


class BookView(BaseView):

    def get_all(self, cat_id):
        return self.model.objects().filter(
                    self.model.category_id==cat_id).all()


category_view = BaseView(Category)
book_view = BookView(Book)

