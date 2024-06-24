import mysql.connector

def get_connection():
    return mysql.connector.connect(
        host="localhost",
        user="root",
        password="suryaa",
        database="eduschema"
    )

def add_course(course_name, description):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO Courses (course_name, description) VALUES (%s, %s)"
    cursor.execute(query, (course_name, description))
    conn.commit()
    cursor.close()
    conn.close()

def remove_course(course_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE Courses SET deleted=TRUE WHERE course_id=%s"
    cursor.execute(query, (course_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_courses():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Courses WHERE deleted=FALSE"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_all_deleted_courses():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Courses WHERE deleted=TRUE"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def add_student(name, email):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO Students (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name, email))
    conn.commit()
    cursor.close()
    conn.close()

def remove_student(student_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE Students SET deleted=TRUE WHERE student_id=%s"
    cursor.execute(query, (student_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_students():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Students WHERE deleted=FALSE"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_all_deleted_students():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Students WHERE deleted=TRUE"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def add_instructor(name, email):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO Instructors (name, email) VALUES (%s, %s)"
    cursor.execute(query, (name, email))
    conn.commit()
    cursor.close()
    conn.close()

def remove_instructor(instructor_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE Instructors SET deleted=TRUE WHERE instructor_id=%s"
    cursor.execute(query, (instructor_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_instructors():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Instructors WHERE deleted=FALSE"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_all_deleted_instructors():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Instructors WHERE deleted=TRUE"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def add_assessment(course_id, assessment_name, description):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO Assessments (course_id, assessment_name, description) VALUES (%s, %s, %s)"
    cursor.execute(query, (course_id, assessment_name, description))
    conn.commit()
    cursor.close()
    conn.close()

def remove_assessment(assessment_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE Assessments SET deleted=TRUE WHERE assessment_id=%s"
    cursor.execute(query, (assessment_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_assessments():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Assessments WHERE deleted=FALSE"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_all_deleted_assessments():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Assessments WHERE deleted=TRUE"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def add_grade(student_id, assessment_id, grade):
    conn = get_connection()
    cursor = conn.cursor()
    query = "INSERT INTO Grades (student_id, assessment_id, grade) VALUES (%s, %s, %s)"
    cursor.execute(query, (student_id, assessment_id, grade))
    conn.commit()
    cursor.close()
    conn.close()

def remove_grade(grade_id):
    conn = get_connection()
    cursor = conn.cursor()
    query = "UPDATE Grades SET deleted=TRUE WHERE grade_id=%s"
    cursor.execute(query, (grade_id,))
    conn.commit()
    cursor.close()
    conn.close()

def get_all_grades():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Grades WHERE deleted=FALSE"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result

def get_all_deleted_grades():
    conn = get_connection()
    cursor = conn.cursor()
    query = "SELECT * FROM Grades WHERE deleted=TRUE"
    cursor.execute(query)
    result = cursor.fetchall()
    cursor.close()
    conn.close()
    return result
