#!/usr/bin/python3
""" this script that takes in an argument and displays all values in
    the states table of hbtn_0e_0_usa where name matches the argument."""


if (__name__ == "__main__"):
    import MySQLdb
    import sys

    if (len(sys.argv) == 5):
        try:
            conn = MySQLdb.connect(
                    host="localhost",
                    user=sys.argv[1],
                    passwd=sys.argv[2],
                    db=sys.argv[3],
                    )
            cur = conn.cursor()
            state_name = sys.argv[4]
            query = f"""SELECT * FROM states WHERE name = '{state_name}'
            ORDER BY id ASC"""
            cur.execute(query)
            query_rows = cur.fetchall()
            for row in query_rows:
                print(row)
            cur.close()
            conn.close()
        except MySQLdb.Error as err:
            print(f"{err}")
