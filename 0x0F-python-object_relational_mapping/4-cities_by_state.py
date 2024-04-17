#!/usr/bin/python3
"""lists all cities from the database hbtn_0e_4_usa"""

if (__name__ == "__main__"):
    import MySQLdb
    import sys

    conn = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = conn.cursor();
    query = """
    SELECT c.id, c.name, s.name
    FROM cities c
    INNER JOIN states s ON c.state_id = s.id
    ORDER BY c.id ASC;
    """
    cur.execute(query)
    query_rows = cur.fetchall()
    for row in query_rows:
        print(row)
    cur.close()
    conn.close()
