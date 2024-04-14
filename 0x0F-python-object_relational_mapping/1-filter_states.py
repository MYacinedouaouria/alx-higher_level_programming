#!/usr/bin/python3
"""This script lists all states with a name starting with 'N'
    from the database hbtn_0e_0_usa."""

if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(
            host="localhost",
            ser=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = conn.cursor()

    cur.execute(
            "SELECT * FROM states WHERE name LIKE 'N%' ORDER BY id ASC"
            )
    query_rows = cur.fetchall()

    for row in query_rows:
        print(row)

    cur.close()
    conn.close()
