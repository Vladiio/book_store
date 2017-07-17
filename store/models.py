from sqlalchemy import Column, Integer, \
         String, ForeignKey
from sqlalchemy.orm import relationship

from database.conf import Base, session


class AlchemyItem:
    id = Column(Integer, primary_key=True)

    @classmethod
    def objects(cls):
        return session.query(cls)
    
    def save(self):
        session.add(self)
        session.commit()


class Book(Base, AlchemyItem):
    __tablename__ = "books"

    title = Column(String, unique=True)
    author = Column(String)
    price = Column(Integer)
    category_id = Column(Integer,
                         ForeignKey("categories.id"))

    category = relationship("Category",
                            back_populates="books")

    def __repr__(self):
        return "\t{0.id}\t{0.title}\t" \
               "{0.author}\t{0.price}".format(self)


class Category(Base, AlchemyItem):
    __tablename__ = "categories"
    
    name = Column(String, unique=True)
    books = relationship("Book", order_by=Book.id,
                         back_populates="category")

    def __repr__(self):
        count = len(self.books)
        return f"\t{self.id}\t{self.name}\t{count}"

