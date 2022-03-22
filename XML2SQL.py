import xml.etree.ElementTree as ET
import sqlite3


def lookup(d, key):
    found = False
    for child in d:
        if found:
            return child.text
        if child.tag == 'key' and child.text == key:
            found = True
    return None


# Creates sqlite file if not exists
conn = sqlite3.connect('XML2SQL.sqlite')
cur = conn.cursor()

# Make some fresh tables using executescript()
cur.executescript('''
DROP TABLE IF EXISTS Artist;
DROP TABLE IF EXISTS Genre;
DROP TABLE IF EXISTS Album;
DROP TABLE IF EXISTS Track;

CREATE TABLE Artist (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Genre (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name    TEXT UNIQUE
);

CREATE TABLE Album (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    artist_id  INTEGER,
    title   TEXT UNIQUE
);

CREATE TABLE Track (
    id  INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title TEXT  UNIQUE,
    album_id  INTEGER,
    genre_id  INTEGER,
    len INTEGER, rating INTEGER, count INTEGER
);
''')

xml_file = './AssignmentData/Data_XML2SQL.xml'
xml_parsed = ET.parse(xml_file)
entries = xml_parsed.findall('dict/dict/dict')
print('Entry count:', len(entries))
for entry in entries:
    if lookup(entry, 'Track ID') is None:  # If not a track (but a playlist)
        continue

    track_title = lookup(entry, 'Name')
    artist_name = lookup(entry, 'Artist')
    genre_name = lookup(entry, 'Genre')
    album_title = lookup(entry, 'Album')
    track_count = lookup(entry, 'Play Count')
    track_rating = lookup(entry, 'Rating')
    track_length = lookup(entry, 'Total Time')

    if track_title is None or artist_name is None or album_title is None or genre_name is None:
        continue

    print(track_title, '|', artist_name, '|', genre_name, '|', album_title, '|', track_count, '|', track_rating,
          '|', track_length)

    # INSERT OR IGNORE: insert row if the "UNIQUE" constraint is satisfied
    cur.execute('''INSERT OR IGNORE INTO Artist (name) VALUES ( ? )''', (artist_name,))
    cur.execute('SELECT id FROM Artist WHERE name = ? ', (artist_name,))
    artist_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Genre (name) VALUES ( ? )''', (genre_name,))
    cur.execute('SELECT id FROM Genre WHERE name = ? ', (genre_name,))
    genre_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Album (title, artist_id) VALUES ( ?, ? )''', (album_title, artist_id))
    cur.execute('SELECT id FROM Album WHERE title = ? ', (album_title,))
    album_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Track (title, album_id, genre_id, len, rating, count) 
        VALUES ( ?, ?, ?, ?, ?, ? )''', (track_title, album_id, genre_id, track_length, track_rating, track_count))

    conn.commit()
