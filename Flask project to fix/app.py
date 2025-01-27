from flask import Flask, render_template
import requests

app = Flask(__name__)

API_BASE_URL = "http://localhost:8000/api"


@app.route("/")
def dashboard():
    try:
        students = requests.get(f"{API_BASE_URL}/students/").json()
        subjects = requests.get(f"{API_BASE_URL}/subjects/").json()
        grades = requests.get(f"{API_BASE_URL}/grades/").json()
    except requests.exceptions.ConnectionError:
        return "Error: Cannot connect to Django API. Please ensure Django server is running on port 8000."
    except requests.exceptions.JSONDecodeError:
        return "Error: Invalid response from API. Please check API endpoints."

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
    student_data.sort(key=lambda x: x["average"], reverse=True)
    
    for index, student in enumerate(student_data):
        student["rank"] = index + 1
        
    return render_template("dashboard.html", students=student_data)


if __name__ == "__main__":
    app.run(debug=True, port=5000)
