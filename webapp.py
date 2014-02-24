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

@app.route("/")
def get_github():
    return render_template("get_github.html")


if __name__ == "__main__":
    app.run(debug=True)

