from store.models import Book, Category
from database.conf import session


class MainView:
    def __init__(self):
        self.session = session
        
    def get_categories(self, cat_name):
        if cat_name == "all":
            result = self.session.query(Category).all() 
        else:
            result = self.session.query(Category).\
                        filter(Category.name==cat_name)
        return result

    def get_books(self, cat_id):
        if cat_id == 0:
            result = self.session.query(Book).all()
        else:
            result = self.session.query(Book).\
                    filter(Category.id==cat_id).all()
        return result   

    def create_book(self, category, 
                    title, author, price):
        pass
    
    def create_category(self, cat_name):
        pass


main_view = MainView()

