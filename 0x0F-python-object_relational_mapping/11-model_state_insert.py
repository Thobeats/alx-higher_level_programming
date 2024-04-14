#!/usr/bin/python3
"""
Write a script that adds
the State object “Louisiana”
to the database hbtn_0e_6_usa
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

    new_state = State(name='Louisiana',)

    state = session.add(new_state)
    session.commit()
    print("{}".format(new_state.id))
    session.close()
