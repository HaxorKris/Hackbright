import hackbright_app
from flask import Flask, render_template, request


app = Flask(__name__)

# Code goes here

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

@app.route("/project_grades")
def get_grades_byproject():
    hackbright_app.connect_to_db()
    project = request.args.get("project")
    rows = hackbright_app.get_grades_by_project(project)
    html = render_template("project_grades.html", rows=rows)
    return html

@app.route("/")
def get_github():
    return render_template("get_github.html")


if __name__ == "__main__":
    app.run(debug=True)

