#!/usr/bin/python3
import MySQLdb
import sys

if __name__ == "__main__":
    username = sys.argv[1]
    password = sys.argv[2]
    db_name = sys.argv[3]

    # Connect to MySQL database
    db = MySQLdb.connect(host='localhost', port=3306, user=username, passwd=password, db=db_name)
    cursor = db.cursor()

    # Retrieve states starting with 'N'
    query = "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
    cursor.execute(query)

    # Fetch and display results
    states = cursor.fetchall()
    for state in states:
        print(state)

    # Close cursor and connection
    cursor.close()
    db.close()
