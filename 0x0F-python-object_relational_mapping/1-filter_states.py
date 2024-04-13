#!/usr/bin/python3
"""
Write a script that lists all states with a name starting with N (upper N)
     from the database hbtn_0e_0_usa:

    Your script should take 3 arguments: mysql username,
        mysql password and database name (no argument validation needed)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on
         localhost at port 3306
    Results must be sorted in ascending order by states.id
    Results must be displayed as they are in the example below
    Your code should not be executed when imported

"""

import sys
import MySQLdb
"""import the mysql DB-API"""


def main(*args, **kwargs):
    """create a connection and retreive the states"""
    db_conn = MySQLdb.connect(host="localhost",
                              port=3306,
                              user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3],
                              charset="utf8")
    cur = db_conn.cursor()
    cur.execute("SELECT * FROM states WHERE name COLLATE \
                utf8mb4_bin LIKE 'N%' ORDER BY id ASC")
    # cur.execute("SELECT * FROM states WHERE name LIKE 'N%' AND \
    #             name LIKE 'n%' ORDER BY id ASC")
    data = cur.fetchall()

    for row in data:
        print(row)

    cur.close()
    db_conn.close()


if __name__ == "__main__":
    # user, password, database = sys.argv[1], sys.argv[2], sys.argv[3]
    main()
