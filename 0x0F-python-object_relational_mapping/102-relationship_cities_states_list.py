#!/usr/bin/python3
"""
Script that lists all City objects from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City


def list_cities_states(username, password, db):
    """
    Lists all City objects from the database hbtn_0e_101_usa
    """
    # Create an SQLite engine
    engine = create_engine('mysql+mysqldb://{}:{}@localhost:3306/{}'.
                           format(username, password, db), pool_pre_ping=True)

    # Create a configured "Session" class
    Session = sessionmaker(bind=engine)

    # Create a Session instance
    session = Session()

    # Query to retrieve City objects with associated State information
    query = session.query(City).order_by(City.id).all()

    # Display the results
    for city in query:
        print("{}: {} -> {}".format(city.id, city.name, city.state.name))

    # Close the session
    session.close()


if __name__ == "__main__":
    # Check for the correct number of command line arguments
    if len(sys.argv) != 4:
        print("Usage: {} <username> <password> <database>".format(sys.argv[0]))
        sys.exit(1)

    # Extract command line arguments
    username, password, db = sys.argv[1:]

    # Call the list_cities_states function with the provided arguments
    list_cities_states(username, password, db)
