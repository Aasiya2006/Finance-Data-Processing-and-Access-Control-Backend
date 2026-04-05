Finance Management System API
A backend REST API for managing financial records with role-based access control. Built with FastAPI and SQLite.

This was a project I built to practice backend development. The idea is pretty simple — users with different roles (viewer, analyst, admin) can interact 
with financial records based on what they're allowed to do. Admins can do everything, analysts can read and get summaries, and viewers can only read.
It uses FastAPI for the routes, SQLAlchemy for the database stuff, and SQLite.

TechStack Used
- Python
- FastAPI : For building the API
- SQLAlchemy : For database interactions
- SQLite : local database
- Pydantic : data validation through schemas
- Uvicorn : server to run the app

Getting Started
1. Clone the repo
   git clone https://github.com/Aasiya2006/Finance-Data-Processing-and-Access-Control-Backend.git
   cd Finance-Data-Processing-and-Access-Control-Backend

2. Install dependencies
   pip install fastapi uvicorn sqlalchemy

3. Run the server
   uvicorn main:app --reload

Once it's running, head to http://127.0.0.1:8000/docs to see the interactive Swagger UI where you can test all the endpoints.

Project Structure : 

├── main.py        # All the API routes
├── models.py      # Database table definitions
├── schemas.py     # Request body validation
├── database.py    # DB connection and session setup
├── Utils.py       # Permission checking logic
└── finance.db     # Auto-generated SQLite database

Made as part of a backend development assessment. Still learning, but got this working end-to-end!! 
