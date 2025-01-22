Project Context

You are a developer intern who has just joined a school that is behind in digitalizing its operations. For instance, the school still manages grades using paper files, which does not meet current expectations.

You have been tasked with creating a tool to input and consult grades.
You’re not the first person assigned to this mission—another intern had started working on it, and now it’s your job to continue their work. It was decided to create two applications, one in Flask and one in Django, as part of the first version (V1) of the student management application.



---------
Overview

The Django application: Provides a minimal back-office to manage students, subjects, and grades via a graphical interface. It also supplies data via a REST API.

The Flask application: Consumes data from the Django API to display it through a graphical interface.

The previous intern worked on the Flask app, but the work they did lacks quality and doesn’t function properly. You will need to fix this broken code and update it to meet the project requirements.

The Django application, which will be relatively simple, needs to be developed from scratch. To ensure the Flask app can interact with it correctly, the Django application should use the Django REST Framework to provide a REST API.




---------
Detailed Requirements

1. Django Application: Data Management

This application will be responsible for:

    Creating and managing students.
    Creating and managing subjects.
    Recording grades for each student in various subjects.
    Providing data in the form of a REST API for the Flask application.

2. Flask Application: Analysis and Visualization

This application will be responsible for:

    Consuming data from the Django API.
    Calculating and displaying students’ average grades for each subject and overall.
    Providing student rankings.

Each student can have multiple grades per subject.
No authentication (signup/login) is required.



---------
Delivery

The project can be completed individually or in groups of two.
For each student, a GitHub repository with the project is expected, along with a detailed README document containing instructions to deploy the project and a summary of the work done.
The deadline for submission is February 1st.



---------
Additional Resources for Django REST API

    Django REST Framework Documentation
    YouTube Tutorial
    OpenClassrooms Course

Let me know if you need any further refinements!
