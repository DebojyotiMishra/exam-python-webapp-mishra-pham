from flask import Flask, render_template
import requests

app = Flask(__name__)

API_BASE_URL = "http://localhost:8000"


@app.route("/")
def dashboard():
    students = requests.get(f"{API_BASE_URL}/stu/").json()
    subjects = requests.get(f"{API_BASE_URL}/sub/").json()
    grades = requests.get(f"{API_BASE_URL}/gra/").json()

    student_grades = {student["id"]: [] for student in students}
    for grade_entry in grades:
        student_grades[grade_entry["student"]].append(grade_entry["grade"])

    averages = {
        student_id: sum(grades) / len(grades) if grades else 0
        for student_id, grades in student_grades.items()
    }

    student_data = [
        {
            "name": next(
                student["name"] for student in students if student["id"] == student_id
            ),
            "average": average,
        }
        for student_id, average in averages.items()
    ]

    return render_template("dashboard.html", students=student_data)
