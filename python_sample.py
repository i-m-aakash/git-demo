import sqlite3



# User input

user_id = "0; DROP TABLE users; --"



# Vulnerable query

conn = sqlite3.connect("example.db")

cursor = conn.cursor()

query = f"SELECT * FROM users WHERE id={user_id}"

cursor.execute(query)