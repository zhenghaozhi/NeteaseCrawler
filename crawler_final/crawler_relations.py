import sqlite3

conn = sqlite3.connect('database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS relations (
    id INTEGER PRIMARY KEY,
    music_id INTEGER,
    artist_id INTEGER,
    FOREIGN KEY (music_id) REFERENCES music(id),
    FOREIGN KEY (artist_id) REFERENCES artist(id)
)
''')

cursor.execute('SELECT id, artist_id, sub_artist_id FROM music')
musics = cursor.fetchall()

for index, music in enumerate(musics):
    music_id = music[0]
    artist_ids = [music[1], music[2]]
    print(artist_ids)
    for index_add, artist_id in enumerate(artist_ids):
        if not artist_id:
            continue
        cursor.execute('''
            INSERT OR IGNORE INTO relations (id, music_id, artist_id)
            VALUES (?, ?, ?)
            ''', (index * 2 + index_add, music_id, artist_id))
        print("SELFID: " + str(index) + " , ID: " + str(music_id) + " , Process: " + str(index + 1) + "/" + "2801, " + str(format(float(index + 1) * 100/2801, '.2f')) +"%")

conn.commit()

cursor.execute('''
    DELETE FROM artist
    WHERE id NOT IN (SELECT DISTINCT artist_id FROM relations)
''')

conn.commit()

query = "SELECT * FROM relations"
try:
    cursor.execute(query)
    rows = cursor.fetchall()
    for row in rows:
        print(row)
except sqlite3.Error as e:
    print(f"Failed: {e}")

conn.close()

