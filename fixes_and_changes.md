# Fixes

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
6. Enhanced grade table display:
    - Added a ranking column to display the rank of each student
    - Applied CSS for improved visualization

# Django Setup and Changes

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

# Deployment Instructions

1. Django Backend:
    ```bash
    cd django_backend
    pip install -r requirements.txt
    python manage.py migrate
    python manage.py runserver
    ```

2. Flask Frontend:
    ```bash
    cd flask_frontend
    pip install -r requirements.txt
    python app.py
    ```

The Django backend should run on port 8000, and the Flask frontend on port 5000.

