import sqlite3
import time


conn = sqlite3.connect('database.db')
cursor = conn.cursor()
conn.commit()

query = "SELECT * FROM music"
try:
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print(f"Failed: {e}")

time.sleep(10)

query = "SELECT * FROM artist"
try:
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print(f"Failed: {e}")

time.sleep(10)

query = "SELECT * FROM relations"
try:
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print(f"Failed: {e}")
conn.close()