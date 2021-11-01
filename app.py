from Data.students_func import student_api
from Data.attendance_log import attendance_api
from flask import Flask, render_template

app = Flask(__name__)

app.register_blueprint(attendance_api)
app.register_blueprint(student_api)


@app.route("/")
def main_menu():
	return render_template("home.html")


@app.route("/attendance", methods=['GET', 'POST'])
def attendance():
	return render_template("page1.html")


@app.route("/student", methods=['GET', 'POST'])
def std_mngmt():
	return render_template("student.html")


@app.route("/month", methods=['GET', 'POST'])
def month():
	return render_template("month.html")


@app.route("/week", methods=['GET', 'POST'])
def week():
	return render_template("week.html")


@app.route("/day", methods=['GET', 'POST'])
def day():
	return render_template("day.html")


if __name__ == "__main__":
	app.run(debug=False)
