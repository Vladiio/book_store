import pytest

from book_store import book, category


@pytest.fixture(scope="function")
def cat():
    return category.Category("Awesome books")

@pytest.fixture(scope="function")
def item():
    return book.Book("Some title", "Some author", 50)

def test_add_book(cat, item):     
    cat.add_book(item)
    assert item.id in cat.items 
    with pytest.raises(book.BookAlreadyExist):
        cat.add_book(item)

def test_find_by_title(cat, item):
    cat.add_book(item)
    found_book = cat.find_by_title(item.title)
    assert found_book is item
    with pytest.raises(book.BookDoesNotExist):
        found_book = cat.find_by_title("wrong title")

