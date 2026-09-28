import sqlite3

connection = sqlite3.connect("database.db")

cursor = connection.cursor()

cursor.execute("""
CREATE TABLE events (
    id INTEGER PRIMARY KEY,
    title TEXT,
    date TEXT,
    location TEXT
)
""")

cursor.execute("""
CREATE TABLE users (
    id INTEGER PRIMARY KEY,
    username TEXT,
    salary INTEGER
)
""")

events = [
    ("Cybersecurity Conference", "2026-10-15", "Porto"),
    ("Web Security Workshop", "2026-10-20", "Lisbon"),
    ("Introduction to Penetration Testing", "2026-10-25", "Coimbra"),
]

users = [("alice_test", 2500), ("bob_test", 2900), ("charlie_test", 2300)]

cursor.executemany(
    "INSERT INTO events (title, date, location) VALUES (?, ?, ?)", events
)

cursor.executemany("INSERT INTO users (username, salary) VALUES (?, ?)", users)

connection.commit()
connection.close()

print("Database created successfully.")
