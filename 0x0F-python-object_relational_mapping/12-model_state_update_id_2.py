#!/usr/bin/python3
"""this script changes the name of a State object from the database"""


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
    a_state = session.query(State).filter(State.id == 2).first()
    if (a_state):
        a_state.name = "New Mexico"
        session.commit()
