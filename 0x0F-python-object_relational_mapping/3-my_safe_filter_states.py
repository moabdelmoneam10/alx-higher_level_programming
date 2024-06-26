#!/usr/bin/python3
""" Script that list all states from database hbtn_0e_0_usa
    where name matches argument passed
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
    cursor.execute("SELECT id, name FROM states\
                    WHERE BINARY name = %(state)s\
                    ORDER BY id ASC", {'state': sys.argv[4]})

    states = cursor.fetchall()

    for state in states:
        print(state)

    cursor.close()
    db.close()
