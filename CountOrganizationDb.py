import sqlite3
import re

conn = sqlite3.connect("Week2Assignment2.sqlite")
cur = conn.cursor()

cur.execute('DROP TABLE IF EXISTS Counts')
cur.execute('CREATE TABLE Counts (org TEXT, count INTEGER)')

with open("./AssignmentData/mbox.txt", 'r') as f:
    for line in f:
        if not line.startswith('From: '):
            continue
        email = line.split()[1]
        domain_name = re.findall(".+@(.+)$", email)[0]

        cur.execute('SELECT count FROM Counts WHERE org = ? ', (domain_name,))
        row = cur.fetchone()
        if row is None:
            cur.execute('INSERT INTO Counts (org, count) VALUES (?, 1)', (domain_name,))
        else:
            cur.execute('UPDATE Counts SET count = count + 1 WHERE org = ?', (domain_name,))
        conn.commit()

    # https://www.sqlite.org/lang_select.html
    # sql_str = 'SELECT email, count FROM Counts ORDER BY count DESC LIMIT 10'

    # for row in cur.execute(sql_str):
    #     print(row[0], row[1])

cur.close()
