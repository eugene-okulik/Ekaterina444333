import mysql.connector as mysql
import dotenv
import os
import csv

dotenv.load_dotenv()

db = mysql.connect(
    host=os.getenv("DB_HOST"),
    user=os.getenv("DB_USER"),
    passwd=os.getenv("DB_PASSW"),
    database=os.getenv("DB_NAME"),
    port=os.getenv("DB_PORT")
)

cursor = db.cursor(dictionary=True)
query = '''
SELECT
s.name AS name,
s.second_name AS second_name,
g.title AS group_title,
b.title AS book_title,
s2.title AS subject_title,
l.title AS lesson_title,
m.value AS mark_value
FROM students s
RIGHT JOIN `groups` g ON g.id = group_id
RIGHT JOIN books b ON b.taken_by_student_id = s.id
RIGHT JOIN marks m ON m.student_id = s.id
RIGHT JOIN lessons l ON l.id = m.lesson_id
RIGHT JOIN subjects s2 ON s2.id = l.subject_id
'''
cursor.execute(query)
db_rows = cursor.fetchall()

base_path = os.path.dirname(os.path.dirname(os.path.dirname(__file__)))
homework_path = os.path.join(base_path, 'eugene_okulik', 'Lesson_16', 'hw_data', 'data.csv')
with open(homework_path) as csv_file:
    data_csv = csv.DictReader(csv_file)
    csv_rows = []
    for row in data_csv:
        csv_rows.append(row)

missing = []
for row in csv_rows:
    for db_row in db_rows:
        if all(str(db_row.get(key)) == str(row[key]) for key in row.keys()):
            break
    else:
        missing.append(row)

print("Не найдено в базе:")
for row in missing:
    print(row)
