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
   git clone <>
>
