import sqlite3
conn = sqlite3.connect('teatchers.db')
cur = conn.cursor()
find = int(input("Введите ID студента: "))
cur.execute(f'''SELECT students.Student_Id FROM students WHERE Student_Id = {find};''' )
found_Id = cur.fetchone()
clear_Id = found_Id[0]
cur.execute(f'''SELECT students.Student_Name FROM students WHERE Student_Id = {find};''' )
found_name = cur.fetchone()
clear_name = found_name[0]
cur.execute(f'''SELECT students.School_Id FROM students WHERE Student_Id = {find};''' )
found_school_id = cur.fetchone()
clear_school_id = found_school_id[0]
cur.execute(f'''SELECT School.school_name FROM School WHERE School_Id = {clear_school_id};''' )
found_school_name = cur.fetchone()
clear_school_name = found_school_name[0]
print("ID студента:", clear_Id)
print("Имя студента: ", clear_name)
print("ID школы: ", clear_school_id)
print("Название школы: ", clear_school_name)