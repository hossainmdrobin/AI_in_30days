import sqlite3

conn = sqlite3.connect("social.db")

cursor = conn.cursor()
cursor.execute("""
CREATE TABLE posts (
id INTEGER PRIMARY KEY,
name TEXT,
likes INTEGER,
comments INTEGER
)
""")

cursor.execute("INSERT INTO posts VALUES (1,'post1',120,30)")
cursor.execute("INSERT INTO posts VALUES (2,'post2',450,80)")
cursor.execute("INSERT INTO posts VALUES (3,'post3',200,40)")

conn.commit()

print("Database created")