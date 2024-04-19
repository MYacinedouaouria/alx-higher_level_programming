#!/usr/bin/python3
"""this script adds the State object “Louisiana”
to the database hbtn_0e_6_usa"""


if (__name__ == "__main__"):
    import sys
    import sqlalchemy
    from model_state import State, Base
    from sqlalchemy import (create_engine)
    from sqlalchemy.orm import sessionmaker

    if (len(sys.argv) == 4):
        engine = create_engine(
                'mysql+mysqldb://{}:{}@localhost/{}'.format(
                    sys.argv[1], sys.argv[2], sys.argv[3]
                    ),
                pool_pre_ping=True
                )
        Session = sessionmaker(bind=engine)
        session = Session()
        state = State(name="Louisiana")
        session.add(state)
        session.commit()
        print(f"{state.id}")
        session.close()
