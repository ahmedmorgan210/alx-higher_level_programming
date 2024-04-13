#!/usr/bin/python3
"""
write a script that takes in arguments and displays all values in
the states table of hbtn_0e_0_usa where name matches the argument.
But this time, write one that is safe from MySQL injections!

    Your script should take 4 arguments: mysql username, mysql password,
        database name and state name searched (safe from MySQL injection)
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


def main(user, password, database, state_name):
    """create a connection and retreive the states"""
    db_conn = MySQLdb.connect(host="localhost",
                              port=3306,
                              user=sys.argv[1],
                              passwd=sys.argv[2],
                              db=sys.argv[3],
                              charset="utf8")
    cur = db_conn.cursor()

    #   The %s is a placeholder for a parameter, and the actual value\
    #       is passed as a tuple (sys.argv[4],). This method ensures that\
    #       the user input is properly escaped and treated as a literal value,\
    #       not as part of the SQL command.

    # query = "SELECT cities.id, cities.name, states.name\
    #             FROM cities\
    #             JOIN states ON cities.state_id = states.id\
    #             WHERE states.name = %s"
    #             #ORDER BY cities.id ASC;"
    # cur.execute(query, (sys.argv[4],))

    cur.execute("SELECT cities.name FROM cities\
                JOIN states ON cities.state_id = states.id\
                WHERE states.name = %s\
                ORDER BY cities.id ASC;", (state_name,))
    data = cur.fetchall()

    city_names = ', '.join([row[0] for row in data])
    print(city_names)
    # for row in data:
    #     print(row)

    cur.close()
    db_conn.close()


if __name__ == "__main__":
    user, password, database, state_name = sys.argv[1], \
        sys.argv[2], sys.argv[3], sys.argv[4]
    main(user, password, database, state_name)


# Additional Tips:
# 1) Always Use Parameterized Queries:
#        Whenever you need to include
#        user input in your SQL queries, use parameterized queries.
#        This applies to all types of SQL queries,
#        including SELECT, INSERT, UPDATE, and DELETE.
# 2) Limit Database Permissions:
#        Ensure that the database user used by your application
#        has the minimum necessary permissions.
#        This can limit the potential damage of an SQL injection attack.
# 3) Validate and Sanitize Input:
#        While parameterized queries are effective at preventing SQL injection,
#        it's still a good practice to validate and sanitize user input
#        before using it in your application.
#        This can help catch invalid or malicious input early.
# Use ORM Libraries:
#        If possible, consider using an Object-Relational Mapping (ORM)
#        library like SQLAlchemy or Django ORM.
#        These libraries provide a higher-level,
#        more secure interface for interacting with databases,
#        and they automatically handle many of the security concerns,
#        including SQL injection.
