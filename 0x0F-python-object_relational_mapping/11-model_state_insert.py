#!/usr/bin/python3
"""  Write a script that adds the State object,
“Louisiana” to the database hbtn_0e_6_usa """

if __name__ == "__main__":
    from sqlalchemy import create_engine
    from sqlalchemy.orm import sessionmaker
    from model_state import Base, State
    from sys import argv

    engine = create_engine(
            "mysql+mysqldb://{}:{}@localhost/{}".format(
                argv[1], argv[2], argv[3]))

    session = sessionmaker(bind=engine)()
    louisiana = State(name="Louisiana")
    session.add(louisiana)
    session.commit()
    print(louisiana.id)
    session.close()
