# School Grade Management System

A modern web-based school grade management system built with Django REST Framework and Flask. This project consists of two applications:
- A Django backend providing a REST API and admin interface for managing student data
- A Flask frontend for visualizing student performance and grades

## Team member Names
1. Debojyoti Mishra
2. Phuong Khanh Pham

## Project Structure
```bash
├── Flask project to fix
│   ├── __pycache__
│   │   └── app.cpython-311.pyc
│   ├── app.py
│   ├── requirements.txt
│   ├── static
│   │   └── styles.css
│   └── templates
│       └── dashboard.html
├── README.md
├── django_backend
│   ├── db.sqlite3
│   ├── django_backend
│   │   └── urls.py
│   ├── grades
│   │   ├── __pycache__
│   │   │   ├── admin.cpython-313.pyc
│   │   │   ├── models.cpython-313.pyc
│   │   │   ├── serializers.cpython-313.pyc
│   │   │   ├── urls.cpython-313.pyc
│   │   │   └── views.cpython-313.pyc
│   │   ├── admin.py
│   │   ├── migrations
│   │   │   ├── 0001_initial.py
│   │   │   ├── __init__.py
│   │   │   └── __pycache__
│   │   ├── models.py
│   │   ├── serializers.py
│   │   ├── urls.py
│   │   └── views.py
│   ├── manage.py
│   ├── requirements.txt
│   └── school_management
│       ├── __pycache__
│       │   ├── settings.cpython-313.pyc
│       │   ├── urls.cpython-313.pyc
│       │   └── wsgi.cpython-313.pyc
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
├── fixes_and_changes.md
```

## Project Overview

### Backend (Django)
The Django application provides:
- REST API endpoints for students, subjects, and grades
- Admin interface for data management
- Database models with proper relationships
- API serialization and validation

### Frontend (Flask)
The Flask application:
- Consumes the Django REST API
- Calculates and displays student averages
- Provides a user-friendly dashboard
- Visualizes student performance data

## Technical Stack

### Backend
- Python 3.8+
- Django 4.2+
- Django REST Framework 3.14+
- SQLite (default database)

### Frontend
- Python 3.8+
- Flask
- Requests library
- Jinja2 templating

## Installation & Setup

### 1. Clone the Repository
```bash
git clone <repository-url>
cd exam-python-webapp-mishra-pham
```

### 2. Backend Setup (Django)
### Create and activate virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Navigate to Django project
```bash
cd django_backend
```

### Install dependencies
```bash
pip install -r requirements.txt
```

### Run migrations
```bash
python manage.py makemigrations
python manage.py migrate
```

### Create superuser
```bash
python manage.py createsuperuser
```

### Start Django server
```bash
python manage.py runserver 8000
```

## 2. Frontend Setup (Flask)

### In a new terminal, activate virtual environment
```bash
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### Navigate to Flask project
```bash
cd ../Flask\ project\ to\ fix
```

### Install Flask dependencies
```bash
pip install flask requests
```

### Start Flask server
```bash
python app.py
```

## API Endpoints

The Django backend provides the following REST API endpoints:

### Students: `/api/students/`
- **GET**: List all students
- **POST**: Create new student
- **PUT/PATCH**: Update student
- **DELETE**: Remove student

### Subjects: `/api/subjects/`
- **GET**: List all subjects
- **POST**: Create new subject
- **PUT/PATCH**: Update subject
- **DELETE**: Remove subject

### Grades: `/api/grades/`
- **GET**: List all grades
- **POST**: Create new grade
- **PUT/PATCH**: Update grade
- **DELETE**: Remove grade


## Data Models

### Student
- `name`: Student's full name
- `student_id`: Unique identifier

### Subject
- `name`: Subject name
- `code`: Unique subject code

### Grade
- `student`: Foreign key to Student
- `subject`: Foreign key to Subject
- `grade`: Numerical grade value
- `date`: Date of grade entry

## Features

### Admin Interface
- Accessible at `/admin/`
- Complete CRUD operations for all models
- Search and filter capabilities
- User-friendly interface

### API Features
- Full REST API support
- Browsable API interface
- Proper serialization
- Input validation

### Frontend Features
- Student grade dashboard
- Average grade calculations
- Performance visualization
- Responsive design

## Work Summary

Organized backend and frontend into separate folders.

### Flask fixes
1. Added missing imports:
    - requests for making HTTP requests
    - Properly imported Flask and render_template from flask

2. Fixed Flask initialization:
    - Changed flask to Flask (proper capitalization)

3. Fixed route:
    - Changed @app.route('///') to @app.route('/')
    - Fixed variable naming and iteration issues:
    - Corrected the student_grades dictionary comprehension to use students instead of student
    - Fixed the grade iteration to avoid variable shadowing
    - Renamed iteration variable to grade_entry as its more clear

4. Fixed template rendering:
    - Changed template name from "dash.html" to "dashboard.html" to match the actual file
    - Fixed the template variables (removed subjects parameter as it's not used in the template)

5. Added application entry point:
- Included the `if __name__ == '__main__'`: block to run the application with debugging enabled:
        ```python
        if __name__ == '__main__':
            app.run(debug=True)
        ```

### Django Backend
- Created a Django project with **Django REST Framework** and **CORS headers**.
- Defined models for **Students, Subjects, and Grades**.
- Ran migrations to set up the database.

1. Initial Setup:
- Created Django project using `django-admin startproject django_backend`
- Created 'grades' app using `python manage.py startapp grades`
- Installed required dependencies:
    ```bash
    pip install django djangorestframework
    ```
- Added 'rest_framework' and 'grades' to INSTALLED_APPS in settings.py

2. Models Implementation:
    - Created Student model with fields for name and student ID
    - Created Subject model with fields for name and code
    - Created Grade model with foreign keys to Student and Subject, plus grade value
    - Applied migrations using `python manage.py makemigrations` and `python manage.py migrate`

3. REST API Implementation:
    - Created serializers for Student, Subject, and Grade models
    - Implemented ViewSets for each model to handle CRUD operations
    - Set up REST API URLs using DefaultRouter
    - Configured proper URL patterns in urls.py

4. API Endpoints Created:
    - GET/POST/PUT/DELETE /api/students/
    - GET/POST/PUT/DELETE /api/subjects/
    - GET/POST/PUT/DELETE /api/grades/

5. Admin Interface:
    - Registered models in admin.py for easy data management
    - Customized admin views for better usability

## Challenges & Solutions
- **CORS Errors:** Fixed with **django-cors-headers**.
- **Database Relationships:** Used **Foreign Keys** to link Students, Subjects, and Grades.
- **Frontend-Backend Integration:** Managed **HTTP requests and API responses** in Flask.
- **Git Issues:** Resolved merge conflicts and improved workflow.
