#!/usr/bin/python3
""" State model with SQLAlchemy
"""
import sys
from model_state import State, Base
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    for instance in session.query(State):
        print(f"{instance.id}: {instance.name}")
