#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values in 
the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!

    Your script should take 4 arguments: mysql username, mysql password,
        database name and state name searched (safe from MySQL injection)
    You must use the module MySQLdb (import MySQLdb)
    Your script should connect to a MySQL server running on localhost at port 3306
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

    # query = "SELECT * FROM states WHERE name COLLATE SQL_Latin1_General_Cp1_CS_AS\
    #     LIKE %s ORDER BY id ASC"

    query = "SELECT * FROM states WHERE name COLLATE utf8mb4_bin\
        LIKE %s ORDER BY id ASC"
    cur.execute(query, (sys.argv[4],))
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
