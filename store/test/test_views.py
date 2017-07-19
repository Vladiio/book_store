import pytest

from store.views import book_view
from store.models import Book, Category
from store import exc


@pytest.fixture(scope="module")
def category(request): 
    new_cat = Category(title="Test_cat2")
    def del_item():
        print("Cleaning..")
        new_cat.delete()
    request.addfinalizer(del_item)
    return new_cat


class TestBook:

    def test_get(self, category):
        new_book = Book(title="SomeTitle",
                        author="Name",
                        category_id=category.id)  
        fetched = book_view.get("SomeTitle")
        assert new_book is fetched

    def test_get_invalid_title(self):
        with pytest.raises(exc.ObjectDoesNotExist):
            book_view.get("invalid_title")

