# Expense Tracker REST API

A REST API built with Python and Flask for tracking personal expenses with JWT-based authentication.

## Tech Stack
- Python, Flask, Flask-RESTful
- SQLAlchemy, SQLite
- Flask-JWT-Extended (Authentication)
- Flask-Bcrypt (Password Hashing)

## Features
- User registration and login with hashed passwords
- JWT token-based authentication
- Add, view, and delete expenses
- Filter expenses by category
- Monthly expense summary by category

## Project Structure
expense_tracker_api/
├── app/
│   ├── init.py
│   ├── models.py
│   ├── resources.py
│   └── auth.py
├── config.py
├── run.py
└── requirements.txt

## Setup & Installation

```bash
git clone https://github.com/linkinpark1234/expense-tracker-api.git
cd expense-tracker-api
pip install -r requirements.txt
python run.py
```

## API Endpoints

| Method | Endpoint | Description | Auth Required |

| POST | /auth/register | Register new user | No |
| POST | /auth/login | Login, returns JWT token | No |
| POST | /expenses | Add new expense | Yes |
| GET | /expenses | Get all expenses | Yes |
| GET | /expenses?category=food | Filter by category | Yes |
| GET | /expenses/summary | Monthly total by category | Yes |
| DELETE | /expenses/<id> | Delete an expense | Yes |

## Usage Example

**Register:**
```json
POST /auth/register
{
    "username": "vitthal",
    "email": "vitthal@test.com",
    "password": "test123"
}
```

**Login and use token:**
```json
POST /auth/login
→ returns { "token": "eyJ..." }

GET /expenses
Header: Authorization: Bearer <token>
```
