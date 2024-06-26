#!/usr/bin/python3
""" State model with SQLAlchemy
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        query = session.query(State).filter(State.name == sys.argv[4]).first()
        print(f"{query.id}")
    except Exception as e:
        print("Not found")
