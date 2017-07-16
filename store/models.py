from sqlalchemy import Column, Integer, \
         String, ForeignKey
from sqlalchemy.orm import relationship

from database.conf import Base, session


class Book(Base):
    __tablename__ = "books"

    id = Column(Integer, primary_key=True)
    title = Column(String)
    author = Column(String)
    price = Column(Integer)
    category_id = Column(Integer,
                         ForeignKey("categories.id"))

    category = relationship("Category",
                            back_populates="books")

    def __repr__(self):
        return "{0.id}, {0.title}, " \
               "{0.author}, {0.price}".format(self)

    def save(self):
        session.add(self)


class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    books = relationship("Book", order_by=Book.id,
                         back_populates="category")
    def __repr__(self):
        count = len(self.books)
        return f"{self.id}\t{self.name}\t{count}"
