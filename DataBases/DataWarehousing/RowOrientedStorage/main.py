import sqlite3

conn = sqlite3.connect('example.db')
cursor = conn.cursor()
cursor.execute('CREATE TABLE users (id INTEGER PRIMARY KEY, name TEXT, email TEXT)')
cursor.execute("INSERT INTO users VALUES (1, 'John Doe', 'john.doe@example.com')")
cursor.execute("INSERT INTO users VALUES (2, 'Jane Smith', 'jane.smith@example.com')")
cursor.execute('SELECT * FROM users')
result = cursor.fetchall()
print(result)
