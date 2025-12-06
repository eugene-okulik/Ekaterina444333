import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

# Insert student
cursor.execute(
    "INSERT INTO students (name, second_name) VALUES ('Nicolay', 'Nicolay')"
)
student_id = cursor.lastrowid

# Insert book
cursor.execute(
    f"INSERT INTO books (title, taken_by_student_id) "
    f"VALUES ('My_book', {student_id})"
)

# Insert group
cursor.execute(
    "INSERT INTO `groups` (title, start_date, end_date) "
    "VALUES ('MIMIMU', 'sep 2025', 'jul 2026')"
)
group_id = cursor.lastrowid

cursor.execute(
    f"UPDATE students SET group_id = {group_id} WHERE id = {student_id}"
)

# Insert subjects
cursor.execute("INSERT INTO subjects (title) VALUES ('MA')")
subjects1_id = cursor.lastrowid

cursor.execute("INSERT INTO subjects (title) VALUES ('MO')")
subjects2_id = cursor.lastrowid

# Insert lessons
cursor.execute(
    "INSERT INTO lessons (title, subject_id) VALUES "
    f"('1', {subjects1_id}), ('2', {subjects1_id}), "
    f"('1', {subjects2_id}), ('2', {subjects2_id})"
)

# Get lesson IDs
cursor.execute("SELECT id FROM lessons ORDER BY id DESC LIMIT 4")
lessons_ids = cursor.fetchall()
last_ids = [row['id'] for row in lessons_ids]

# Insert marks
cursor.execute(
    "INSERT INTO marks (value, lesson_id, student_id) VALUES "
    f"('5', {last_ids[0]}, {student_id}), "
    f"('5', {last_ids[1]}, {student_id}), "
    f"('5', {last_ids[2]}, {student_id}), "
    f"('5', {last_ids[3]}, {student_id})"
)

db.commit()

# Queries
marks_query = """
SELECT *
FROM marks
WHERE student_id = 21713
"""
cursor.execute(marks_query)
print(cursor.fetchall())

books_query = """
SELECT *
FROM books
WHERE taken_by_student_id = 21713
"""
cursor.execute(books_query)
print(cursor.fetchall())

all_info_query = """
SELECT *
FROM students s
RIGHT JOIN `groups` g ON g.id = group_id
RIGHT JOIN books b ON b.taken_by_student_id = s.id
RIGHT JOIN marks m ON m.student_id = s.id
RIGHT JOIN lessons l ON l.id = m.lesson_id
RIGHT JOIN subjects s2 ON s2.id = l.subject_id
WHERE s.id = 21713
"""
cursor.execute(all_info_query)
print(cursor.fetchall())
