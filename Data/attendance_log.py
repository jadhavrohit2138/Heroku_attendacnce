import csv
import datetime
from flask import Blueprint, request, render_template


attendance_api = Blueprint("attendance_api", __name__)


# mark the attendance with password
@attendance_api.route("/mark_attendance", methods=['GET', 'POST'])
def mark_attendance():
	result = ''
	result1 = ''
	if request.method == 'POST' and 'id_to_mark' in request.form and 'pas' in request.form:
		id_to_mark = request.form.get("id_to_mark")
		pas = request.form.get("pas")
		lines = []
		dt = datetime.datetime.now()
		with open('students.csv', 'r') as readFile:
			reader = csv.reader(readFile)
			found = False
			for row in reader:
				lines.append(row)
				for field in row:
					if field == id_to_mark and pas == row[5]:
						first_name = row[1]
						last_name = row[2]
						found = True
		if found is True:
			with open('attendance.csv', 'a+', newline='') as f:
				fieldnames = ['Student ID', 'First Name', 'Last Name', 'Date', 'Time']
				thewriter = csv.DictWriter(f, fieldnames=fieldnames)
				f.seek(0, 2)
				if f.tell() == 0:
					thewriter.writeheader()
				thewriter.writerow({'Student ID': id_to_mark, 'First Name': first_name, 'Last Name': last_name, 'Date': dt.strftime("%x"), 'Time': dt.strftime("%X")})
				result = id_to_mark
		else:
			result1 = id_to_mark
	return render_template("mark_attendance.html", result=result, result1=result1)


# Daily attendance of class
@attendance_api.route("/daily_attendance", methods=['GET', 'POST'])
def daily_attendance():
	output = ''
	output1 = ''
	var11 = ''
	var12 = ''
	if request.method == 'POST' and 'date' in request.form and 'month' in request.form:
		date = request.form.get("date")
		month = request.form.get("month")
		with open('attendance.csv', 'r') as readFile:
			reader = csv.reader(readFile)
			found = False
			next(reader)
			output = []
			var1 = 0
			for row in reader:
				cr = row[3]
				cr1_month = cr.split("/")[0]
				cr1_day = cr.split("/")[1]
				if date == cr1_day and month == cr1_month:
					var1 += 1
					found = True
					output.append(row)
		with open('students.csv', 'r') as readFile1:
			reader1 = csv.reader(readFile1)
			found1 = False
			for i, num in enumerate(reader1):
				found1 = True

		if found is True:
			var11 = var1
		else:
			output1 = f"Data is Not Available"
		if found1 is True:
			var12 = i

	return render_template("daily_attendance.html", output=output, output1=output1, var11=var1, var12=var12)


# Daily attendance report of particular student
@attendance_api.route("/std_attendance", methods=['GET', 'POST'])
def std_attendance():
	result = ''
	result2 = ''
	if request.method == 'POST' and 'id_to_mark' in request.form and 'id_date' in request.form and 'id_month' in request.form:
		id_to_mark = request.form.get("id_to_mark")
		id_date = request.form.get("id_date")
		id_month = request.form.get("id_month")
		with open('attendance.csv', 'r') as readFile:
			reader = csv.reader(readFile)
			found = False
			for row in reader:
				for field in row:
					if field == id_to_mark:
						date = row[3]
						month = row[3]
						name = row[1]
						current_date = date.split('/')[1]
						current_month = month.split('/')[0]
						if id_date == current_date and id_month == current_month:
							found = True
							result = row
		if found is True:
			pass
		else:
			result2 = f"{name} is absent at {id_date} / {id_month}"
	return render_template("std_attendance.html", result=result, result2=result2)


# monthly attendance of class
@attendance_api.route("/monthly_attendance", methods=['GET', 'POST'])
def monthly_attendance():
	output = ''
	output1 = ''
	if request.method == 'POST' and 'month' in request.form:
		month = request.form.get("month")
		with open('attendance.csv', 'r') as readFile:
			reader = csv.reader(readFile)
			found = False
			next(reader)
			output = []
			for row in reader:
				# output.append(row)
				cr_month = row[3]
				cr1_month =cr_month.split("/")[0]
				if month == cr1_month:
					found = True
					output.append(row)
		if found is True:
			pass
		else:
			output1 = f"Data is Not Available"

	return render_template("monthly_attendance.html", output=output, output1=output1)


# monthly attendance of Student
@attendance_api.route("/std_monthly_attendance", methods=['GET', 'POST'])
def std_monthly_attendance():
	output = ''
	output1 = ''
	var11 = ''
	if request.method == 'POST' and 'month' in request.form and 'month' in request.form:
		id_to_mark = request.form.get("id_to_mark")
		month = request.form.get("month")
		with open('attendance.csv', 'r') as readFile:
			reader = csv.reader(readFile)
			found = False
			next(reader)
			var1 = 0
			output = []
			for row in reader:
				for field in row:
					if field == id_to_mark:
						cr_month = row[3]
						cr1_month = cr_month.split("/")[0]
						if month == cr1_month:
							var1 += 1
							found = True
							output.append(row)
		if found is True:
			var11 = var1
		else:
			output1 = f"Data is Not Available"

	return render_template("std_monthly_attendance.html", output=output, output1=output1, var11=var11)


# Weekly attendance of class
@attendance_api.route("/weekly_attendance", methods=['GET', 'POST'])
def weekly_attendance():
	output = ''
	output1 = ''
	if request.method == 'POST' and 'start' in request.form and 'end' in request.form and 'month' in request.form:
		start = request.form.get("start")
		end = request.form.get("end")
		month = request.form.get("month")
		with open('attendance.csv', 'r') as readFile:
			reader = csv.reader(readFile)
			found = False
			next(reader)
			output = []
			for row in reader:
				cr = row[3]
				cr1_month = cr.split("/")[0]
				cr1_day = cr.split("/")[1]
				if start <= cr1_day and end >= cr1_day and month == cr1_month:
					found = True
					output.append(row)
		if found is True:
			pass
		else:
			output1 = f"Something is Wrong"

	return render_template("weekly_attendance.html", output=output, output1=output1)


# Weekly attendance of class
@attendance_api.route("/std_weekly_attendance", methods=['GET', 'POST'])
def std_weekly_attendance():
	output = ''
	output1 = ''
	var11 = ''
	if request.method == 'POST' and 'id_to_mark' in request.form and 'start' in request.form and 'end' in request.form and 'month' in request.form:
		id_to_mark = request.form.get("id_to_mark")
		start = request.form.get("start")
		end = request.form.get("end")
		month = request.form.get("month")
		with open('attendance.csv', 'r') as readFile:
			reader = csv.reader(readFile)
			found = False
			next(reader)
			output = []
			var1 = 0
			for row in reader:
				for field in row:
					if field == id_to_mark:
						cr = row[3]
						cr1_month = cr.split("/")[0]
						cr1_day = cr.split("/")[1]
						if start <= cr1_day and end >= cr1_day and month == cr1_month:
							var1 += 1
							found = True
							output.append(row)
		if found is True:
			var11 = var1
		else:
			output1 = f"Something is Wrong"

	return render_template("std_weekly_attendance.html", output=output, output1=output1, var11=var11)
