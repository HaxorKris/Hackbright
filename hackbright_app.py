import sqlite3

DB = None
CONN = None

def get_student_by_github(github):
    query = """SELECT first_name, last_name, github FROM Students WHERE github = ?"""
    DB.execute(query, (github,))
    row = DB.fetchone()
    return row
#    return """\
#Student: %s %s
#Github account: %s"""%(row[0], row[1], row[2])

def make_new_student(first_name,last_name,github):
    query = """INSERT INTO Students values (?, ?, ?)"""
    DB.execute(query, (first_name, last_name, github))
    CONN.commit()
    print "Successfully added student: %s %s"%(first_name, last_name)

def connect_to_db():
    global DB, CONN
    CONN = sqlite3.connect("hackbright.db")
    DB = CONN.cursor()

def get_project_by_title(title):
    query = """SELECT title, description, max_grade from Projects WHERE title = ?"""
    DB.execute(query, (title,))
    row = DB.fetchone()
    print """\
Project: %s 
Project description: %s
Max grade: %s """%(row[0], row[1], row[2])

def make_new_project(title, description, max_grade):
    query = """INSERT INTO Projects values (NULL, ?, ?, ?)"""
    DB.execute(query, (title, description, max_grade))
    CONN.commit()
    print "Successfully added project: %s %s"%(title, description)

def get_grade_by_student_project(student_github, project_title):
    query = """SELECT Students.first_name, Students.last_name, Grades.project_title, Grades.grade 
        FROM Grades JOIN Projects ON (Grades.project_title = Projects.title)
        JOIN Students ON (Students.github = Grades.student_github)
        WHERE student_github = ?
        AND project_title = ?"""
    DB.execute(query, (student_github, project_title))
    row = DB.fetchone()
    print """\
    Name: %s %s
    Project: %s
    Grade: %s """%(row[0], row[1], row[2], row[3])

def get_grades_by_project(project_title):
    query = """SELECT Students.first_name, Students.last_name, Grades.project_title, Grades.grade 
        FROM Grades JOIN Projects ON (Grades.project_title = Projects.title)
        JOIN Students ON (Students.github = Grades.student_github)
        WHERE project_title = ?"""
    DB.execute(query, (project_title,))
    rows = DB.fetchall()
    return rows

def get_grades_by_student(student_github):
    query = """select * from Grades where student_github = ? """
    DB.execute(query, (student_github,))
    print "Github / Project / Grade"
    row = DB.fetchall()
    return row
    # for item in row:
    #     print """%s / %s / %s"""% (item[0], item[1], item[2])

    # print """\
    # Github / Project / Grade
    # %s / %s /  """%(row[0], row[1])



def give_grade(student_github, project_title, grade):
    query = """INSERT INTO Grades VALUES (?, ?, ?)"""
    DB.execute(query, (student_github, project_title, grade))
    CONN.commit()
    print "Successfully added grade: %s %s %s"%(student_github, project_title, grade)

def main():
    connect_to_db()
    command = None
    while command != "quit":
        print "************"
        print "Please separate command and each value with two (2) spaces"
        print "************"
        input_string = raw_input("HBA Database> ")
        tokens = input_string.split("  ")
        command = tokens[0]
        args = tokens[1:]

        if command == "student":
            get_student_by_github(*args) 
        elif command == "new_student":
            make_new_student(*args)
        elif command == "get_project":
            get_project_by_title(*args)
        elif command == "new_project":
            make_new_project(*args)
        elif command == "get_project_grade":
            get_grade_by_student_project(*args)
        elif command == "give_grade":
            give_grade(*args)
        elif command == "get_grades":
            get_grades_by_student(*args)
        elif command == "get_grades_new":
            get_grades_by_project(*args)

    CONN.close()

if __name__ == "__main__":
    main()
