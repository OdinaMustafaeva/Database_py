# Imports

import psycopg2
import psycopg2.extras

# Connection

connection = psycopg2.connect(
    dbname='book_shop',
    user='postgres',
    host='localhost',
    port=5432,
    password='43201'
)

# SQl codes

cur = connection.cursor(cursor_factory=psycopg2.extras.RealDictCursor)
sql = "insert into book(name, col) values (%s, %s)"
cur.execute(sql, ("test", "white"))
connection.commit()

# Result

records = cur.fetchall()
print(records)

# close connection

connection.close()
