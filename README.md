﻿# 🏋️ Fitness Booking API

A simple RESTful API built with Django and Django REST Framework to manage class bookings at a fictional fitness studio. This system allows users to:

- View upcoming fitness classes
- Book a class
- View all bookings by email address

---

## 🚀 Tech Stack

- Python 3.10+
- Django 5.x
- Django REST Framework
- SQLite (default)

---

## ⚙️ Setup Instructions

1. **Clone the repository**
   ```bash
   https://github.com/PrasannaSgkumar/Fitness
   cd fitness-booking-api
# Fitness Booking API


python -m venv env
.\env\Scripts\activate  
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver


1. Create a New Fitness Class
URL: POST classes/create/
Body:


{
  "name": "Yoga",
  "datetime": "2025-06-22T07:00:00Z",
  "instructor": "Anita",
  "available_slots": 10
}


2. Get All Upcoming Classes
URL: GET /classes/
Response:

[
  {
    "id": 3,
    "name": "Yoga",
    "datetime": "2025-06-22T07:00:00Z",
    "instructor": "Anita",
    "available_slots": 10
  }
]



3. Book a Class
URL: POST /book/
Body:

{
  "class_id": 3,
  "client_name": "Prasanna Kumar",
  "client_email": "prasanna@example.com"
}

Response

{
    "id": 5,
    "client_name": "Prasanna Kumar",
    "client_email": "prasanna@example.com",
    "fitness_class": 3
}


Get Bookings by Email
URL: GET /bookings/?client_email=prasanna@example.com
Response:

[
    {
        "id": 5,
        "client_name": "Prasanna Kumar",
        "client_email": "prasanna@example.com",
        "fitness_class": 3
    }
]



Loom Video Link:
https://drive.google.com/file/d/1bO-sS7itsEyU_n2HPLDvYmab99f2Yerv/view?usp=sharing
