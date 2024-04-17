#!/usr/bin/python3
""" this script takes in the name of a state as an argument and lists
all cities of that state, using the database hbtn_0e_4_usa

"""

if (__name__ == "__main__"):
    import MySQLdb
    import sys

    conn = MySQLdb.connect(
            host="localhost",
            user=sys.argv[1],
            passwd=sys.argv[2],
            db=sys.argv[3]
            )
    cur = conn.cursor()
    state_name = sys.argv[4]
    query = """
    SELECT c.name
    FROM cities c
    INNER JOIN states s ON c.state_id = s.id
    WHERE s.name = %s
    ORDER BY c.id ASC;
    """
    cur.execute(query, (state_name,))
    query_rows = cur.fetchall()
    first_city = True
    for city in query_rows:
        if not first_city:
            print(", ", end="")
        print(city[0], end="")
        first_city = False
    print()
    cur.close()
    conn.close()
