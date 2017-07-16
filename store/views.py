from store.models import Book, Category
from store import exc
from database.conf import session


class MainView:
        
    def get_category_list(self):
        return Category.objects().all()

    def get_category(self, cat_name):
        return Category.objects().filter(
                      Category.name==cat_name).first()
        
    def get_book_list(self, cat_id):
        return Book.objects().filter(
                    Book.category_id==cat_id).all()

    
    def get_book(self, book_title):
        return Book.objects().filter(
                    Book.title==book_title).one()

    def create_book(self, cat_name, 
                    title, author, price):
        category = self.get_category(cat_name)
        if not category:
            raise exc.ObjectDoesNotExist(cat_name)
        book = Book(title=title, author=author,
                    category_id=category.id, price=price)
        book.save()
         
    def create_category(self, cat_name):
        pass


main_view = MainView()

