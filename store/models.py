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
    @classmethod
    def objects(cls):
        return session.query(cls)

    def __repr__(self):
        return "\t{0.id}\t{0.title}\t" \
               "{0.author}\t{0.price}".format(self)

    def save(self):
        session.add(self)


class Category(Base):
    __tablename__ = "categories"
    
    id = Column(Integer, primary_key=True)
    name = Column(String)
    
    books = relationship("Book", order_by=Book.id,
                         back_populates="category")
   
    @classmethod
    def objects(cls):
        return session.query(cls)

    def __repr__(self):
        count = len(self.books)
        return f"\t{self.id}\t{self.name}\t{count}"
