
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
