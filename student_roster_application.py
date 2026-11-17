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


while True:
    print("\n=== Student Roster Manager ===")
    print("1. Add a student")
    print("2. View all students")
    print("3. Update a student's GPA")
    print("4. Delete a student")
    print("5. Quit")

    choice = input("\nSelect an option (1-5): ")

    if choice == "1":
        name = input("Student name: ")
        grade = int(input("Grade: "))
        gpa = float(input("GPA: "))

        add_student(name, grade, gpa)
        print("Student added successfully.")
    elif choice == "2":
        students = get_all_students()

        if not students:
            print("No students found.")
        else:
            print("\nID | Name | Grade | GPA")
            print("-" * 30)
            for student in students:
                print(
                    f"{student[0]} | {student[1]} | "
                    f"{student[2]} | {student[3]}"
                )
    elif choice == "3":
        student_id = int(input("Student ID: "))
        new_gpa = float(input("New GPA: "))

        update_student_gpa(student_id, new_gpa)
        print("GPA updated successfully.")
    elif choice == "4":
        student_id = int(input("Student ID to delete: "))

        delete_student(student_id)
        print("Student deleted successfully.")
    elif choice == "5":
        print("Goodbye!")
        break
    else:
        print("Invalid option. Please choose 1-5.")
    
connection.close()