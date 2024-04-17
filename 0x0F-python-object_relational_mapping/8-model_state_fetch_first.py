#!/usr/bin/python3
"""this script prints the first State object from the database hbtn_0e_6_usa"""


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
    first_state = session.query(State).first()
    if (first_state):
        print(f"{first_state.id}: {first_state.name}")
    else:
        print("Nothing")
