# 🏥 FHIR Ingestion API

A minimal and practical FastAPI project for ingesting, storing, and managing FHIR-compliant patient data into a SQLite database.

---

## 📦 Tech Stack

- *Python 3.10*
- *FastAPI* for building the API
- *Pydantic* for data validation
- *SQLAlchemy* as ORM
- *SQLite* as the database
- *Uvicorn* for local server running
- *Swagger UI* (automatically included via FastAPI)

---

## 🚀 Features

- ✅ Add FHIR-compliant patients
- ✅ View all patients
- ✅ View single patient by ID
- ✅ Update (PUT) patient records
- ✅ Delete patient records
- ✅ Built-in interactive API docs at /docs

---

## 🔧 How to Run Locally

1.Clone the repository 
   ```
    git clone https://github.com/your-username/fhir-ingestion-api.git
   cd fhir-ingestion-api
 ```
2.Create a Virtual environment
   ```
   python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
 ```
3.Install dependencies
```
pip install -r requirements.txt
 ```
4.Create the database
 ```
python create_tables.py
```
5.Run the API
```
uvicorn main:app --reload
```
6.Access the Swagger UI 
Open your browser and go to:
http://127.0.0.1:8000/docs

fhir_ingestion_project/
│
├── main.py               # FastAPI entry point
├── models.py             # SQLAlchemy models
├── schemas.py            # Pydantic schemas
├── database.py           # DB connection and session
├── create_tables.py      # Script to initialize DB tables
├── requirements.txt      # Python dependencies
└── README.md             # Project documentation

🔒 Disclaimer

This project is for educational and demonstration purposes only. It is not intended for production use without proper security, authentication, and data validation layers.

⸻

📬 Contact

Created with ❤ by Sara Ahangari
🔗 GitHub: https://github.com/sarahng2001
