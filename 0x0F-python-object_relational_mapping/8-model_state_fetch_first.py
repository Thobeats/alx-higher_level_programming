#!/usr/bin/python3
"""
Write a script that prints
the first State object
from the database
hbtn_0e_6_usa
"""

from sys import argv
from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker
State = __import__('model_state').State


if __name__ == "__main__":
    con = """mysql+mysqldb://{}:{}@localhost/{}"""
    engine = create_engine(con.format(argv[1],
                                      argv[2],
                                      argv[3]
                                      ), pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    Base = declarative_base()
    Base.metadata.create_all(engine)

    state = session.query(State).order_by(State.id).first()
    if state is None:
        print("Nothing")
    else:
        print("{}: {}".format(state.id, state.name))
    session.close()
