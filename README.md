# FastAPI-service-support-tickets
A FastAPI web service that takes free-form JSON and turns it into structured support tickets saved in a SQLite database. It also has an endpoint to show product info from docs. Built with FastAPI, SQLAlchemy, and aiosqlite, it's great for help desks run by people.


# FastAPI Unified Support Service

A FastAPI web service that accepts free-form JSON requests, maps them to structured support tickets stored in a SQLite database, and provides product information from documentation files. Built with FastAPI, SQLAlchemy, and aiosqlite.

## Features

- Unified API to create support tickets from free-form JSON
- Retrieve product information from documentation files
- Uses SQLite for lightweight data storage
- Asynchronous and efficient design

requirements:-

- Python 3.10+
- FastAPI
- SQLAlchemy
- aiosqlite
- SQLite


most be :-

<img width="207" height="457" alt="Screenshot 2025-09-20 130042" src="https://github.com/user-attachments/assets/6ce6d484-c73c-4c7c-8791-34b40ed18106" />


installation steps:-

1. Clone the repository:

   ```bash
   git clone https://github.com/your-username/your-repo.git
   cd your-repo


2.Create and activate a virtual environment:-

python -m venv venv
source venv/bin/activate      # On Windows: venv\Scripts\activate


3.Install:-

pip install -r requirements.txt


4.Run the FastAPI server:-

uvicorn main:app --reload

5.Open your browser and visit http://127.0.0.1:8000/docs

