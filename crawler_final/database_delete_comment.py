import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute("UPDATE music SET comment = ''")
conn.commit()
conn.close()