#!/usr/bin/python3
"""this script lists all State objects that contain the letter a
from the database hbtn_0e_6_usa"""


if (__name__ == "__main__"):
    import sys
    import sqlalchemy
    from model_state import State, Base
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                ),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    a_states = session.query(State).filter(State.name.like('%a%')) \
        .order_by(State.id.asc()).all()
    for state in a_states:
        print(f"{state.id}: {state.name}")
