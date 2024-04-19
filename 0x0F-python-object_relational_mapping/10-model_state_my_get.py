#!/usr/bin/python3
"""this script prints  the State id with the name
passed as argument from the database hbtn_0e_6_usa
"""


if (__name__ == "__main__"):
    import sys
    import sqlalchemy
    from model_state import State, Base
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    if (len(sys.argv) != 5):
        exit(1)
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                ),
            pool_pre_ping=True
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    state_name = sys.argv[4]
    state_id = session.query(State.id) \
        .filter(State.name == state_name) \
        .first()
    if state_id:
        print(state_id[0])
    else:
        print("Not found")
