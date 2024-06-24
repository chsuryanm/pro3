from flask import Flask, render_template, request, redirect, url_for
import database  # Assuming your database functions are defined in a module named database

app = Flask(__name__)

# Home route
@app.route('/')
def home():
    return render_template('base.html')

# Students Management Routes
@app.route('/students.html', methods=['GET', 'POST'])
def manage_students():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        database.add_student(name, email)
        return render_template('students.html', students=students)
        #return redirect(url_for('manage_students'))  # Redirect to avoid resubmission on refresh
    elif request.args.get('action') == 'delete':
        student_id = request.args.get('student_id')
        database.remove_student(student_id)
        return redirect(url_for('manage_students'))  # Redirect to update view after deletion

    students = database.get_all_students()
    return render_template('students.html', students=students)

# Courses Management Route
@app.route('/courses.html', methods=['GET', 'POST'])
def manage_courses():
    if request.method == 'POST':
        name = request.form['name']
        description = request.form['description']
        database.add_course(name, description)
        return redirect(url_for('manage_courses'))
    
    if request.args.get('action') == 'delete':
        course_id = request.args.get('course_id')
        database.remove_course(course_id)
        return redirect(url_for('manage_courses'))
    
    courses = database.get_all_courses()
    return render_template('courses.html', courses=courses)

# Assessments Management Routes
@app.route('/assessments.html', methods=['GET', 'POST'])
def manage_assessments():
    if request.method == 'POST':
        course_id = request.form['course_id']
        assessment_name = request.form['assessment_name']
        description = request.form['description']
        database.add_assessment(course_id, assessment_name, description)
        return render_template('assessments.html', assessments=assessments)
    elif request.args.get('action') == 'delete':
        assessment_id = request.args.get('assessment_id')
        database.remove_assessment(assessment_id)
    assessments = database.get_all_assessments()
    return render_template('assessments.html', assessments=assessments)

# Grades Management Routes
@app.route('/grades.html', methods=['GET', 'POST'])
def manage_grades():
    if request.method == 'POST':
        student_id = request.form['student_id']
        assessment_id = request.form['assessment_id']
        grade = request.form['grade']
        if student_id and assessment_id and grade:  # Basic form validation
            database.add_grade(student_id, assessment_id, grade)
        return redirect(url_for('manage_grades'))
    
    elif request.args.get('action') == 'delete':
        grade_id = request.args.get('grade_id')
        if grade_id:
            database.remove_grade(grade_id)
        return redirect(url_for('manage_grades'))
    
    grades = database.get_all_grades()
    return render_template('grades.html', grades=grades)

# Instructors Management Routes
@app.route('/instructors.html', methods=['GET', 'POST'])
def manage_instructors():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        database.add_instructor(name, email)
    elif request.args.get('action') == 'delete':
        instructor_id = request.args.get('instructor_id')
        database.remove_instructor(instructor_id)
    instructors = database.get_all_instructors()
    return render_template('instructors.html', instructors=instructors)

# Deleted Records Route
@app.route('/deleted.html')
def deleted():
    deleted_courses = database.get_all_deleted_courses() or []
    deleted_students = database.get_all_deleted_students() or []
    deleted_instructors = database.get_all_deleted_instructors() or []
    deleted_assessments = database.get_all_deleted_assessments() or []
    deleted_grades = database.get_all_deleted_grades() or []

    return render_template('deleted.html', deleted_courses=deleted_courses, deleted_students=deleted_students,
                           deleted_instructors=deleted_instructors, deleted_assessments=deleted_assessments,
                           deleted_grades=deleted_grades)

if __name__ == '__main__':
    app.run(debug=True)
