from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, \
         String, ForeignKey
from sqlalchemy.orm import relationship

from store.settings import session


Base = declarative_base()


class AlchemyItem:
    id = Column(Integer, primary_key=True)
    title = Column(String, unique=True)

    def __init__(self, *args, **kwargs):
        super.__init__(*args, **kwargs)
        session.add(self)

    @classmethod
    def objects(cls):
        return session.query(cls)
    
    def save(self):
        session.commit()

    def delete(self):
        session.delete(self)


class Book(Base, AlchemyItem):
    __tablename__ = "books"

    author = Column(String)
    price = Column(Integer)
    category_id = Column(
        Integer, ForeignKey("categories.id"))

    category = relationship(
        "Category", back_populates="books")

    def __repr__(self):
        return ("\t{0.id}\t{0.title}\t"
                "{0.author}\t{0.price}").format(self)


class Category(Base, AlchemyItem):
    __tablename__ = "categories"
    
    books = relationship(
        "Book", order_by=Book.id,
        back_populates="category")

    def __repr__(self):
        count = len(self.books)
        return f"\t{self.id}\t{self.title}\t{count}"

