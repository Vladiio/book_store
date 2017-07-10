import pytest

from book_store import book, category


@pytest.fixture(scope="module")
def cat():
    return category.Category("Awesome books")

@pytest.fixture(scope="module")
def item():
    return book.Book("Some title", "Some author", 50)

def test_add_book(cat, item):
    cat.add_book(item)
    assert item.id in cat.items

