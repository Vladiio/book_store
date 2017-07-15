from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

import settings


Base = declarative_base()

engine = create_engine("sqlite:///db.sqlite3",
                        echo=settings.DEBUG)

session = sessionmaker(bind=engine)()

