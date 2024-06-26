#!/usr/bin/python3
""" Script that list all cities by states
    from database hbtn_0e_4_usa
"""
import sys
import MySQLdb


if __name__ == "__main__":
    db = MySQLdb.connect(user=sys.argv[1],
                         passwd=sys.argv[2],
                         db=sys.argv[3],
                         host='localhost',
                         port=3306)
    cursor = db.cursor()
    cursor.execute(f"SELECT cities.name\
                     FROM states INNER JOIN cities\
                     ON cities.state_id = states.id\
                     WHERE states.name = '{sys.argv[4]}'\
                     ORDER BY cities.id ASC")

    cities = cursor.fetchall()

    print(', '.join(city[0] for city in cities))

    cursor.close()
    db.close()
