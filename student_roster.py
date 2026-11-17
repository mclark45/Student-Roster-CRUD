import sqlite3

connection = sqlite3.connect("school.db")
cursor = connection.cursor()
cursor.execute("PRAGMA foreign_keys = ON")

cursor.execute("""
    CREATE TABLE IF NOT EXISTS students (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        grade INTEGER NOT NULL,
        gpa REAL
    )
""")

connection.commit()


def add_student(name, grade, gpa):
    """
    Add a student to the students table.

    Args:
        name (str): Name of the student.
        grade (int): Student's grade level.
        gpa (float): Student's GPA.

    Returns:
        None
    """

    cursor.execute(
        "INSERT INTO students (name, grade, gpa) VALUES (?, ?, ?)",
        (name, grade, gpa)
    )
    connection.commit()


def get_all_students():
    """
    Get all students from students table

    Args:
        None

    Returns:
        list[tuple]: A list containing all student records.
            Each tuple contains:
            (id, name, grade, gpa)

    """

    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()


def get_student_by_id(student_id):
    """
    Retrieve a student by ID.

    Args:
        student_id (int): The student's unique ID.

    Returns:
        tuple | None:
            The student record as (id, name, grade, gpa),
            or None if no matching student is found.
    """

    cursor.execute(
        "SELECT * FROM students WHERE id = ?",
        (student_id,)
    )
    return cursor.fetchone()


def update_student_gpa(student_id, new_gpa):
    """
    Update a student's GPA.

    Args:
        student_id (int): The student's ID.
        new_gpa (float): The new GPA value.

    Returns:
        None
    """

    cursor.execute(
        "UPDATE students SET gpa = ? WHERE id = ?",
        (new_gpa, student_id)
    )
    connection.commit()


def delete_student(student_id):
    """
    Delete a student from the students table.

    Args:
        student_id (int): The ID of the student to delete.

    Returns:
        None
    """

    cursor.execute(
        "DELETE FROM students WHERE id = ?",
        (student_id,)
    )
    connection.commit()


add_student("Kendall Roy", 97, 3.8)
add_student("Shiv Roy", 90, 3.5)
add_student("Tom Wambsgans", 75, 2.6)
add_student("Logan Roy", 100, 4.0)


print("=== Students ===")

for row in get_all_students():
    print(row)

update_student_gpa(1, 3.9)

delete_student(4)

print("\n=== After Updates ===")

for row in get_all_students():
    print(row)

connection.close()

