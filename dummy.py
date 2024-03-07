import sqlite3

def dummy_db():
    ## connect to db
    connection = sqlite3.connect("student.db")

    ## Creating cursor
    cursor = connection.cursor()

    ## Table
    table_info="""
    Create table STUDENT(NAME VARCHAR(25),CLASS VARCHAR(25),
    SECTION VARCHAR(25),MARKS INT);"""

    cursor.execute(table_info)

    ## Adding dummy data
    cursor.execute("""INSERT INTO Student (NAME, CLASS, SECTION, MARKS)
    VALUES
     ('Alice', '10th', 'A', 85),
     ('Bob', '10th', 'B', 78),
     ('Charlie', '11th', 'A', 92),
     ('David', '11th', 'B', 80),
     ('Emily', '12th', 'A', 95),
     ('Frank', '12th', 'B', 87),
     ('Grace', '9th', 'A', 82),
     ('Henry', '9th', 'B', 75),
     ('Isabella', '10th', 'A', 90),
     ('Jack', '10th', 'B', 83),
     ('Olivia', '11th', 'A', 98),
     ('William', '11th', 'B', 89),
     ('Sophia', '12th', 'A', 97),
     ('James', '12th', 'B', 84),
     ('Charlotte', '9th', 'A', 81),
     ('Liam', '9th', 'B', 76),
     ('Ava', '10th', 'A', 91),
     ('Noah', '10th', 'B', 86),
     ('Mia', '11th', 'A', 99),
     ('Ethan', '11th', 'B', 88);""")

    data = cursor.execute("""select * from Student""")

    for row in data:
     print(row)


    connection.commit()
    connection.close()
