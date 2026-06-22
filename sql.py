import psycopg2, sys, psswd as psswd
from datetime import timedelta

nmemlib = int(sys.argv[1])
cserver = sys.argv[2]

conn = psycopg2.connect(
    host='localhost',
    database='test',
    user='arelyxl',
    password=psswd.PASSWORD,
    port=5432   
)


cur = conn.cursor()

sql = """
INSERT INTO s04dlog (nmemlib, cserver)
VALUES (%s, %s)
"""

cur.execute(sql, (nmemlib, cserver))
conn.commit()

cur.close()
conn.close()
