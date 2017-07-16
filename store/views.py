from store.models import Book, Category
from database.conf import session


class MainView:
    def __init__(self):
        self.session = session
        
    def get_all(self, model=Category):
        return self.session.query(model).all() 

    def get_books(self, cat_id):
        return self.session.query(Book).\
                filter(Category.id==cat_id).all()


main_view = MainView()

