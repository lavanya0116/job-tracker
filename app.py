from flask import Flask, request, jsonify
from models import db, Job

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///jobs.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

@app.route('/')
def home():
    return "Job Tracker Running"

@app.route('/add', methods=['POST'])
def add_job():
    data = request.json
    job = Job(company=data['company'], role=data['role'], status=data['status'])
    db.session.add(job)
    db.session.commit()
    return jsonify({"message": "Job added"})

@app.route('/jobs', methods=['GET'])
def get_jobs():
    jobs = Job.query.all()
    return jsonify([
        {"company": j.company, "role": j.role, "status": j.status}
        for j in jobs
    ])
@app.route('/add-test')
def add_test():
    job = Job(company="Google", role="Software Engineer", status="Applied")
    db.session.add(job)
    db.session.commit()
    return "Test job added"
if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
    