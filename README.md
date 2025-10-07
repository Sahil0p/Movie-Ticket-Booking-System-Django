
Here is your README.md content with GitHub emoji markdown included for better presentation. You can copy-paste this directly:

text
# 🎬 Movie Ticket Booking System – Backend Assignment

This repository contains a Django backend for a Movie Ticket Booking System featuring user authentication (JWT), complete REST APIs, booking logic, and interactive Swagger API documentation.

## 🛠 Tech Stack

- 🐍 Python  
- 🌐 Django  
- ⚙️ Django REST Framework  
- 🔐 JWT (djangorestframework-simplejwt)  
- 📄 Swagger (drf-yasg)  
- 🗃️ SQLite (default)

---

## 🚀 Setup Instructions

### 1️⃣ Clone the repository
```bash
git clone https://github.com/Sahil0p/Movie-Ticket-Booking-System-Django
cd Movie-Ticket-Booking-System-Django
```

### 2️⃣ Create and activate a virtual environment
```bash
python -m venv env

# For Windows:
env\Scripts\activate

# For Mac/Linux:
source env/bin/activate
```

### 3️⃣ Install dependencies
```bash
pip install -r requirements.txt
```

### 4️⃣ Apply migrations
```bash
python manage.py makemigrations  
python manage.py migrate
```


### 4️⃣ Create superuser (optional)
```bash
python manage.py runserver
```

### 5️⃣ Create superuser (optional)
```bash
python manage.py runserver
```

---

## 📂 File Structure
```plaintext
movie-booking-system/
├── movie_booking_system/ # Django project config
├── booking/ # App: models, views, serializers, urls
├── templates/ # HTML templates
├── manage.py # Django management script
├── requirements.txt # Project dependencies
└── README.md # This file
```

## 🔐 JWT Authentication & API Usage

- **Signup:**  
  `POST /signup`  
  `Payload example:{ "username": "youruser", "password": "yourpass" }`

- **Login:**  
   `POST /login`  
   `Payload example:{ "username": "youruser", "password": "yourpass" }`
   `Response will provide JWT access and refresh tokens.`

- **Use JWT in authenticated requests:**  
   `Add in your HTTP headers:`  
   `Authorization: Bearer <access-token>`
- **Refresh Token:**  
`POST /api/token/refresh/`  
`Payload:{ "refresh": "<refresh-token>" }`
`Response returns a new access token.`


---

## 📚 API Endpoints

| Endpoint                    | Method | Auth Required | Description                          |
|-----------------------------|--------|---------------|------------------------------------|
| /signup                     | POST   | ❌            | Register new user                   |
| /login                      | POST   | ❌            | Login and receive JWT tokens       |
| /movies/                    | GET    | ✅            | List all movies                    |
| /movies/<id>/shows/         | GET    | ✅            | List shows for a movie             |
| /shows/<id>/book/           | POST   | ✅            | Book seat(s) for a show            |
| /my-bookings/               | GET    | ✅            | List logged-in user bookings       |
| /bookings/<id>/cancel/      | POST   | ✅            | Cancel your own booking            |
| /swagger/                   | GET    | ❌            | API interactive Swagger docs       |

---

## 📄 Swagger API Documentation

- Browse fully interactive API docs at: [http://localhost:8000/swagger/]`
- Django Login with your credentials
- Use the "Authorize" button in Swagger to enter JWT: Bearer <token>
- In POST /token/  -> write your username & password  -> JWT Token will be generated

---

## 🎯 Business Logic

- ❌ No double booking: a seat cannot be reserved twice.  
- 🚫 No overbooking: bookings capped by show capacity.  
- 🔄 Booking cancellation frees the seat.  
- 🔒 Users can only view and cancel their own bookings.  
- 🛡️ Input validation with helpful error messages.

---

## 🌟 Bonus Features

- 🔁 Retry and atomic transaction logic for concurrency.  
- 🚨 Clear and user-friendly error handling.  
- 🔑 Strict security and ownership validations.  
- 📚 Modular codebase and clean design.

---
## 🎯 Business Logic & Approach

### Setup

This project utilizes Python, Django, and the Django REST Framework to deliver a robust, API-first backend. All dependencies are captured in `requirements.txt`, with a recommended virtual environment for isolated installation.

Database migrations ensure the schema is prepared before running. The JWT mechanism is employed to secure API endpoints while providing stateless authentication. Swagger integration facilitates seamless API exploration.

### Development Approach

- **Authentication and Security:**  
Custom signup and login endpoints issue JWT tokens for secure, protected API access. JWT middleware validates every request.

- **Relational Data Models:**  
The `Movie`, `Show`, and `Booking` models capture all data with defined foreign keys. Each `Booking` is explicitly linked to a user and a show.

- **REST API Architecture:**  
The endpoints follow REST conventions, with POST used for mutations and GET for retrieval. The booking logic uses atomic transactions and retries to prevent concurrency issues.

- **Business Rules Enforcement:**  
The system ensures no double bookings or overbookings occur. Canceling a booking frees up seats efficiently. Input validation and error handling provide a pleasant user experience.

- **Documentation and Testing:**  
Complete Swagger docs detail each API endpoint's requests and responses, including JWT security. Modular and clean code ensures maintainability and testability.

---

## 🌟 Bonus Features

- Atomic retry logic on seat booking to avoid race conditions  
- Structured error messages for invalid operations  
- Enforcement of booking ownership for cancellation  
- Clean separation of concerns across Django apps and views  

---
---
