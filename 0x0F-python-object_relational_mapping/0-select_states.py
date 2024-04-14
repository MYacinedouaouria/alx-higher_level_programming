#!/usr/bin/env python3
""" this script lists all states from the database hbtn_0e_0_us"""


if (__name__ == "__main__"):
    import MySQLdb
    import sys

    if (len(sys.argv) == 4):
        try:
            conn = MySQLdb.connect(
                    host="localhost",
                    user=sys.argv[1],
                    passwd=sys.argv[2],
                    db=sys.argv[3],
                    port=3306
                    )
            cur = conn.cursor()
            cur.execute("SELECT * FROM states ORDER BY id ASC")
            query_rows = cur.fetchall()
            for row in query_rows:
                print(row)
            cur.close()
            conn.close()
        except MySQLdb.Error as err:
            print(f"{err}")
