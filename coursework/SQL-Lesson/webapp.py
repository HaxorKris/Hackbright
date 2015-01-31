import hackbright_app
from flask import Flask, render_template, request


app = Flask(__name__)


@app.route("/")
def get_menu():
    html = render_template("main_menu.html")
    return html

@app.route("/student_lookup")
def student_lookup():
    html = render_template("student_lookup.html")
    return html

@app.route("/student")
# changed this from helloworld() to get_student
# after we copied hackbright_app.py into the ENV directory
def get_student():
# let Flask connect to our database
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    row = hackbright_app.get_student_by_github(student_github)
    html = render_template("student_info.html", first_name=row[0], 
                                last_name=row[1], github=row[2])
    return html

@app.route("/student_grade_lookup")
def student_grade_lookup():
    html = render_template("student_grade_lookup.html")
    return html

@app.route("/get_student")
def get_student_grades():
    hackbright_app.connect_to_db()
    student_github = request.args.get("github")
    rows = hackbright_app.get_grades_by_student(student_github)

    # html = ""
    # for item in rows:
    #     html = html + render_template("get_grades.html", github=item[0],
    #                                     project=item[1], grade=item[2])
    html = render_template("get_grades.html", rows=rows)
    return html

@app.route("/project_grade_lookup")
def project_grade_lookup():
    html = render_template("project_grade_lookup.html")
    return html

@app.route("/project_grades")
def get_grades_byproject():
    hackbright_app.connect_to_db()
    project = request.args.get("title")
    rows = hackbright_app.get_grades_by_project(project)
    html = render_template("project_grades.html", rows=rows)
    return html

@app.route("/new_student")
def add_new_student():
    html = render_template("add_student.html")
    return html

@app.route("/create_student_record")
def create_student():
    hackbright_app.connect_to_db()
    first_name=request.args.get("firstname")
    last_name=request.args.get("surname")
    github=request.args.get("github")
    row = hackbright_app.make_new_student(first_name,last_name,github)
    html = render_template("user_confirmation_screen.html", 
                  first_name=row[0], last_name=row[1], github=row[2])
    return html

@app.route("/new_project")
def add_new_project():
    html = render_template("add_project.html")
    return html

@app.route("/create_project_record")
def create_project():
    hackbright_app.connect_to_db()
    project_title=request.args.get("title")
    project_description=request.args.get("description")
    project_max_grade=request.args.get("max_grade")
    row = hackbright_app.make_new_project(project_title, project_description, project_max_grade)
    html = render_template("project_confirmation_screen.html",
                        project_title=row[0], project_description=row[1],
                        project_max_grade=row[2])
    return html

@app.route("/new_grade")
def add_new_grade():
    html = render_template("add_grade.html")
    return html

@app.route("/create_project_grade")
def create_grade():
    hackbright_app.connect_to_db()
    github=request.args.get("github")
    title=request.args.get("title")
    grade=request.args.get("grade")
    row = hackbright_app.give_grade(github, title, grade)
    html = render_template("grade_confirmation_screen.html", firstname=row[0],
                        lastname=row[1], title=row[2], grade=row[3])
    return html


@app.route("/github")
def get_github():
    return render_template("get_github.html")


if __name__ == "__main__":
    app.run(debug=True)

