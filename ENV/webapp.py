import hackbright_app
from flask import Flask, render_template, request


app = Flask(__name__)

# Code goes here

@app.route("/")
# changed this from helloworld() to get_student
# after we copied hackbright_app.py into the ENV directory
def get_student():
# let Flask connect to our database
    hackbright_app.connect_to_db()
    student_github = request.args.get("student")
    return hackbright_app.get_student_by_github(student_github)

if __name__ == "__main__":
    app.run(debug=True)

