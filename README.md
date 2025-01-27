# fullstack
A web application for managing MOUs (Memorandums of Understanding) and events. This project is built with Django and includes functionality for creating, editing, and managing MOUs and related events.

Features
Create, edit, and delete MOUs.
Add, edit, and delete events associated with MOUs.
View detailed information for each MOU and its events.
Filter and search MOUs for easy navigation.
Built-in user authentication and admin panel for managing data.

Installation
Installation
Clone the repository:

bash
Copy
Edit
git clone https://github.com/<your-username>/<repository-name>.git
cd <repository-name>
Set up a virtual environment:

bash
Copy
Edit
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
Install dependencies:

bash
Copy
Edit
pip install -r requirements.txt
Apply migrations:

bash
Copy
Edit
python manage.py migrate
Create a superuser for the admin panel:

bash
Copy
Edit
python manage.py createsuperuser
Run the development server:

bash
Copy
Edit
python manage.py runserver
Open the application in your browser: http://127.0.0.1:8000/

Project Structure
graphql
Copy
Edit
<mou_manager>/
│
├── <mou>/         # Main Django app for managing MOUs and events
│   ├── migrations/     # Database migrations
│   ├── templates/      # HTML templates
│   ├── views.py        # View functions for handling requests
│   ├── models.py       # Database models
│   ├── forms.py        # Django forms for validation
│   └── urls.py         # URL routing for the app
│    etc.,
├── manage.py           # Django management script
├── db.sqlite3          # SQLite database file
├── requirements.txt    # Python dependencies
└── README.md           # Project documentation
Usage
Adding MOUs
Navigate to the MOU list page.
Click "Create MOU" to add a new MOU.
Fill in the form and save.
Adding Events
Navigate to a specific MOU’s detail page.
Click "Add Event" to create an event for that MOU.
Fill in the event details and save.
Editing/Deleting MOUs and Events
Use the "Edit" or "Delete" buttons available on the respective detail pages.
Technologies Used
Backend: Django
Database: SQLite (default)
Frontend: HTML, CSS (Bootstrap for styling)
Other Tools: Django Admin