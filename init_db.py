#! /usr/bin/env python

from store.settings import engine
from store.models import Base


if __name__ == "__main__":
    Base.metadata.create_all(engine)
