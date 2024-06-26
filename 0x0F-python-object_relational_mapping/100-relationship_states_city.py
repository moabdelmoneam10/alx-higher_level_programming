#!/usr/bin/python3
""" State model with SQLAlchemy
"""
import sys
from relationship_state import State, Base
from relationship_city import City
from sqlalchemy import create_engine, select
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]))
    Session = sessionmaker(bind=engine)
    session = Session()

    state = State(name="California")
    city = City(name="San Francisco")
    state.cities.append(city)
    session.add(state)

    session.commit()
    session.close()
    #print(california.id)
