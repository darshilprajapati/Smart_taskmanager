# Smart Task Management System

A modern full-stack Smart Task Management System built using Flask, PostgreSQL, Socket.IO, and JavaScript.

This application allows users to:
- register/login securely
- create and manage tasks
- update and delete tasks
- track analytics
- receive real-time task updates using WebSockets

---

# Features

## Authentication
- User Registration
- User Login
- Secure Password Hashing
- Session Management

## Task Management
- Create Tasks
- Update Tasks
- Delete Tasks
- Task Priority Management
- Task Status Management

## Analytics
- Total Tasks
- Completed Tasks
- Pending Tasks
- Completion Percentage

## Real-Time Features
- WebSocket Integration
- Live Task Updates

## Modern UI
- Glassmorphism Design
- Responsive Layout
- Animated Dashboard
- Modern Forms & Cards

---

# Tech Stack

## Backend
- Flask
- Flask-SQLAlchemy
- Flask-Login
- Flask-Migrate
- Flask-SocketIO

## Frontend
- HTML5
- CSS3
- JavaScript

## Database
- PostgreSQL
- Neon PostgreSQL

## Deployment
- Render

---

# Project Structure

```bash
smart_task_manager/
│
├── app/
│   ├── __init__.py
│   ├── auth.py
│   ├── routes.py
│   ├── models.py
│   ├── analytics.py
│   ├── socket_events.py
│   └── config.py
│
├── templates/
│   ├── index.html
│   ├── login.html
│   └── register.html
│
├── static/
│   ├── style.css
│   └── app.js
│
├── migrations/
├── requirements.txt
├── run.py
├── manage.py
├── render.yaml
└── README.md
```

---

# Installation

## Clone Repository

```bash
git clone YOUR_GITHUB_REPOSITORY_LINK
```

---

## Create Virtual Environment

```bash
python -m venv venv
```

---

## Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

---

## Install Dependencies

```bash
pip install -r requirements.txt
```

---

# Environment Variables

Create `.env` file:

```env
SECRET_KEY=your_secret_key

DATABASE_URL=your_postgresql_database_url
```

---

# Run Database Migration

```bash
flask db init
```

```bash
flask db migrate -m "Initial migration"
```

```bash
flask db upgrade
```

---

# Run Project

```bash
python run.py
```

Application runs on:

```bash
http://127.0.0.1:5000
```

---

# Deployment

Project deployed using:
- Render
- Neon PostgreSQL

---

# Future Improvements

- Task Deadlines
- Email Notifications
- AI-based Task Suggestions
- Drag & Drop Task Board
- Dark/Light Mode Toggle

---

# Author

Darshil Golaniya

GitHub:
https://github.com/darshilprajapati