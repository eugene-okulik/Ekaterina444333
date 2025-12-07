import mysql.connector as mysql

db = mysql.connect(
    user='st-onl',
    passwd='AVNS_tegPDkI5BlB2lW5eASC',
    host='db-mysql-fra1-09136-do-user-7651996-0.b.db.ondigitalocean.com',
    port=25060,
    database='st-onl'
)

cursor = db.cursor(dictionary=True)

insert_query = "INSERT INTO students (name, second_name) VALUES (%s, %s)"
cursor.execute(insert_query,('Nicolay', 'Nicolayy'))
student_id = cursor.lastrowid

insert_query_2 = "INSERT INTO books (title, taken_by_student_id) VALUES (%s, %s)"
cursor.executemany(insert_query_2, [('Your_book',student_id),('His_book',student_id)])

insert_query_3 = "INSERT INTO `groups` (title, start_date, end_date) VALUES (%s, %s, %s)"
cursor.execute(insert_query_3, ('Nene','oct 2027','sep 2028'))
group_id = cursor.lastrowid

query1 = "UPDATE students SET group_id = %s WHERE id = %s"
cursor.execute(query1,(group_id,student_id))

insert_query_4 = "INSERT INTO subjects (title) VALUES (%s)"
cursor.execute(insert_query_4,('Him',))
subjects1_id = cursor.lastrowid

insert_query_5 = "INSERT INTO subjects (title) VALUES (%s)"
cursor.execute(insert_query_5,('Bio',))
subjects2_id = cursor.lastrowid

insert_query_6 = "INSERT INTO lessons (title, subject_id) VALUES (%s, %s)"
cursor.execute(insert_query_6,('1',subjects1_id))
lessons_id_1 = cursor.lastrowid
cursor.execute(insert_query_6,('2',subjects1_id))
lessons_id_2 = cursor.lastrowid
cursor.execute(insert_query_6,('1',subjects2_id))
lessons_id_3 = cursor.lastrowid
cursor.execute(insert_query_6,('2',subjects2_id))
lessons_id_4 = cursor.lastrowid

insert_marks = "INSERT INTO marks (value, lesson_id, student_id) VALUES (%s, %s, %s)"
cursor.executemany(
    insert_marks, [
        ('5',lessons_id_1,student_id),
        ('2',lessons_id_2,student_id),
        ('3',lessons_id_3,student_id),
        ('4',lessons_id_4,student_id)
    ]
)

db.commit()

marks_query = f"""
SELECT *
FROM marks
WHERE student_id = {student_id}
"""
cursor.execute(marks_query)
print(cursor.fetchall())

books_query = f"""
SELECT *
FROM books
WHERE taken_by_student_id = {student_id}
"""
cursor.execute(books_query)
print(cursor.fetchall())

all_info_query = f"""
SELECT *
FROM students s
RIGHT JOIN `groups` g ON g.id = group_id
RIGHT JOIN books b ON b.taken_by_student_id = s.id
RIGHT JOIN marks m ON m.student_id = s.id
RIGHT JOIN lessons l ON l.id = m.lesson_id
RIGHT JOIN subjects s2 ON s2.id = l.subject_id
WHERE s.id = {student_id}
"""
cursor.execute(all_info_query)
print(cursor.fetchall())
