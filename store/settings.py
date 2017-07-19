from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


DEBUG = False

engine = create_engine("sqlite:///db.sqlite3", echo=DEBUG)
session = sessionmaker(bind=engine)()

