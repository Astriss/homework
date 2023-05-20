import sqlite3
conn = sqlite3.connect('teatchers.db')
cur = conn.cursor()
cur.execute (""" CREATE TABLE IF NOT EXISTS students 
    (
    Student_Id INTEGER PRIMARY KEY, 
    Student_Name TEXT, 
    School_Id INTEGER
    );
    """)
conn.commit()
people = [(201, 'Иван', 1),
          (202, 'Петр', 2),
          (203, 'Анастасия', 3),
          (204, 'Игорь', 4)]
cur.executemany("INSERT INTO students VALUES (?, ?, ?);", people)
conn.commit()


