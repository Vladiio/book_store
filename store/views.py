from store.models import Book, Category
from store import exc
from database.conf import session


class MainView:
        
    def get_categories(self, cat_name):
        if cat_name == "all":
            result = Category.objects().all()
        else:
            result = Category.objects().filter(
                    Category.name==cat_name).first()
        return result

    def get_books(self, cat_id):
        if cat_id == 0:
            result = Book.objects().all()
        else:
            result = Book.objects.filter(
                    Category.id==cat_id).all()
        return result   

    def create_book(self, cat_name, 
                    title, author, price):
        category = self.get_categories(cat_name)
        if not category:
            raise exc.ObjectDoesNotExist(cat_name)
        book = Book(title=title, author=author,
                    category_id=category.id, price=price)
        book.save()
         
    def create_category(self, cat_name):
        pass


main_view = MainView()

