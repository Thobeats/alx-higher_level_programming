#!/usr/bin/python3
"""
Write a Python script
that  prints all City objects 
from the database hbtn_0e_14_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
State = __import__('model_state').State
City = __import__('model_city').City
Base = __import__('model_state').Base


if __name__ == "__main__":
    con = """mysql+mysqldb://{}:{}@localhost/{}"""
    engine = create_engine(con.format(argv[1],
                                      argv[2],
                                      argv[3]
                                      ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base.metadata.create_all(engine)

    cities = session.query(City, State). \
        filter(City.state_id == State.id). \
        order_by(City.id). \
        all()
    
    for city, state in cities:
        print("{} : ({}) {}".format(state.name,
                                    city.id,
                                    city.name))
    session.close()