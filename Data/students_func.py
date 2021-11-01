import csv
from flask import Blueprint, request, render_template
from prettytable import PrettyTable
student_api = Blueprint("student_api", __name__)


@student_api.route("/new_student", methods=['GET', 'POST'])
def to_csv():
	result = ''
	result2 = ''
	result3 = ''
	if request.method == 'POST' and 'std_id' in request.form and 'first_name' in request.form and 'last_name' in request.form and 'phone' in request.form and 'div' in request.form and 'pas' in request.form:
		std_id = request.form.get("std_id")
		first_name = request.form.get("first_name")
		last_name = request.form.get("last_name")
		phone = request.form.get("phone")
		div = request.form.get("div")
		pas = request.form.get("pas")
		if request.form.get("std_id", None) and request.form.get("first_name", None) and request.form.get("last_name", None) and request.form.get("phone", None) and request.form.get("div", None) and request.form.get("pas", None):
			with open('students.csv', 'r', newline='') as fa:
				reader = csv.reader(fa)
				found = False
				next(reader)
				for row in reader:
					if row[0] == std_id:
						found = True
				if found is True:
					result3 = "Id is already taken, try new Id"
				else:
					with open('students.csv', 'a', newline='') as f:
						fieldnames = ['Student ID', 'First Name', 'Last Name', 'Phone Number', 'Div', 'Password']
						thewriter = csv.DictWriter(f, fieldnames=fieldnames)
						f.seek(0, 2)
						if f.tell() == 0:
							thewriter.writeheader()
						thewriter.writerow({'Student ID': std_id, 'First Name': first_name, 'Last Name': last_name, 'Phone Number': phone, 'Div': div, 'Password': pas})
						result = "New Student Added! ID number is: ", std_id
		else:
			result2 = "something is missing, Try again"

	return render_template("new_student.html", result=result, result2=result2, result3=result3)


@student_api.route("/delete_std", methods=['GET', 'POST'])
def delete_std():
	result = ''
	result2 = ''
	if request.method == 'POST' and 'id_to_mark' in request.form and 'pas' in request.form:
		id_to_mark = request.form.get("id_to_mark")
		pas = request.form.get("pas")
		# member = input("Enter Student ID or enter 'quit' to go back.\n ID to delete: ")
		lines = []
		with open('students.csv', 'r') as readFile:
			reader = csv.reader(readFile)
			found = False
			for row in reader:
				lines.append(row)
				for field in row:
					if field == id_to_mark and pas == row[5]:
						lines.remove(row)
						found = True

		with open('students.csv', 'w', newline='') as writeFile:
			writer = csv.writer(writeFile)
			writer.writerows(lines)

		if found is True:
			result = f"Student Id : {id_to_mark} is Deleted."
		else:
			result2 = f"Student Id : {id_to_mark}  Not Found."
			# delete_std()
	return render_template("delete_std.html", result=result, result2=result2)


@student_api.route("/list_student")
def list_student():
	# open csv file
	a = open("students.csv", 'r')

	# read the csv file
	a = a.readlines()

	# Separating the Headers
	l1 = a[0]
	l1 = l1.split(',')

	# headers for table
	t = PrettyTable([l1[0], l1[1], l1[2], l1[3], l1[4], l1[5]])

	# Adding the data
	for i in range(1, len(a)):
		t.add_row(a[i].split(','))

	code = t.get_html_string()
	html_file = open('list_student.html', 'w')
	html_file.write(code)
	return render_template("list_student.html")

# html_file =
# /home/rohit/PycharmProjects/Fynd_Api/templates/list_student.html