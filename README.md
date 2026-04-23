# Job Application Tracker

A simple Flask-based web application to track job applications.

### 🚀 Features
- Add job applications  
- Track company, role, and status  
- Store data using SQLite database  
- Lightweight and easy to use  
- REST-style endpoints for adding and retrieving job applications  
- SQLAlchemy ORM integration for database operations  
- Simple backend architecture for easy extension  

## 🛠 Tech Stack
- Python
- Flask
- SQLite

## 🔗 API Endpoints

- `GET /` → Check if app is running  
- `GET /jobs` → Get all job applications  
- `POST /add` → Add a new job application  
- `GET /add-test` → Insert sample test data  

## ▶️ How to Run

1. Clone the repository:
```bash
git clone https://github.com/your-username/job-tracker.git
```

2. Navigate to the folder:
```bash
cd job-tracker
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the app:
```bash
python app.py
```

5. Open in browser:
```
http://127.0.0.1:5000
```

## 📌 Future Improvements
- Add UI (HTML/CSS)
- Add login/authentication
- Deploy to cloud (AWS / Render)
