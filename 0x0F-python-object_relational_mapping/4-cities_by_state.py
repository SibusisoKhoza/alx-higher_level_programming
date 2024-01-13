#!/usr/bin/python3
"""
 lists all cities from the database hbtn_0e_4_usa
"""

import MySQLdb


def main():
    from sys import argv
    db = MySQLdb.connect(host="localhost", port=3306, user=argv[1],
                         passwd=argv[2], database=argv[3])

    cursor = db.cursor()

    cursor.execute("SELECT cities.id, cities.name, states.name FROM cities\
                    JOIN states ON cities.state_id = states.id")
    for rows in cursor.fetchall():
        print(rows)

    cursor.close()
    db.close()


if __name__ == "__main__":
    main()
    