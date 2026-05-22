# Python WebApp - B.Ed College Website

A Django-based college website with:

- Home Page
- About Us
- Courses
- Faculty
- Gallery
- Notices
- Admission Form
- Contact Form
- Admin Panel (Jazzmin)

## Requirements

- Python 3.12+
- Git
- pip

## Installation

### Clone Repository

```bash
git clone https://github.com/sreejunath/python-webapp.git
cd python-webapp
```

### Create Virtual Environment

```bash
python -m venv venv
```

### Activate Virtual Environment

#### Windows

```bash
venv\Scripts\activate
```

#### Linux / Mac

```bash
source venv/bin/activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Apply Migrations

```bash
python manage.py migrate
```

### Create Admin User

```bash
python manage.py createsuperuser
```

### Run Development Server

```bash
python manage.py runserver
```

Open:

```
http://127.0.0.1:8000
```

## Project Structure

```text
python-webapp/
│
├── college_site/
├── main/
├── templates/
├── static/
├── manage.py
├── requirements.txt
├── .gitignore
└── README.md
```

## Git Workflow

After making changes:

```bash
git add .
git commit -m "Update project"
git push
```

To get latest changes on another system:

```bash
git pull origin main
```

## Author

Sreejunath

GitHub:
https://github.com/sreejunath