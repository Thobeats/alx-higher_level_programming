#!/usr/bin/python3
"""
Write a script that lists
all State objects that
contain the letter a from
the database hbtn_0e_6_usa
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

    state = session.query(State). \
        filter(State.id == 2). \
        first()
    state.name = "New Mexico"
    session.commit()
    session.close()
