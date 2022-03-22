import json
import sqlite3

conn = sqlite3.connect('Json2SQL.sqlite')
cur = conn.cursor()

# Do some setup
cur.executescript('''
DROP TABLE IF EXISTS User;
DROP TABLE IF EXISTS Member;
DROP TABLE IF EXISTS Course;

CREATE TABLE User (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    name   TEXT UNIQUE
);

CREATE TABLE Course (
    id     INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT UNIQUE,
    title  TEXT UNIQUE
);

CREATE TABLE Member (
    user_id     INTEGER,
    course_id   INTEGER,
    role        INTEGER,
    PRIMARY KEY (user_id, course_id)
)
''')

f_name = './AssignmentData/Data_roster.json'

# [
#   [ "Charley", "si110", 1 ],
#   [ "Mea", "si110", 0 ],

str_data = open(f_name).read()
json_data = json.loads(str_data)

for entry in json_data:
    user_name = entry[0]
    course_title = entry[1]
    member_role = entry[2]

    print((user_name, course_title, member_role))

    cur.execute('''INSERT OR IGNORE INTO User (name) VALUES ( ? )''', (user_name,))
    cur.execute('SELECT id FROM User WHERE name = ? ', (user_name,))
    user_id = cur.fetchone()[0]

    cur.execute('''INSERT OR IGNORE INTO Course (title) VALUES ( ? )''', (course_title,))
    cur.execute('SELECT id FROM Course WHERE title = ? ', (course_title,))
    course_id = cur.fetchone()[0]

    cur.execute('''INSERT OR REPLACE INTO Member (user_id, course_id, role) VALUES ( ?, ?, ? )''',
                (user_id, course_id, member_role))

    conn.commit()
