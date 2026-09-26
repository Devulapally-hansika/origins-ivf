from flask import Flask, render_template, request, jsonify
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
from datetime import datetime

app = Flask(__name__)
app.secret_key = 'origins_ivf_secret_key'

# --- 1. DATABASE CONNECTION ---
DATABASE_URL = "mysql+mysqlconnector://admin:OriginsIVF123.@origins-ivf-db.chmaic0ym2vl.ap-south-1.rds.amazonaws.com:3306/origins_ivf"
engine = create_engine(DATABASE_URL)
Base = declarative_base()
Session = sessionmaker(bind=engine)

# --- 2. DATABASE MODELS ---
class Staff(Base):
    __tablename__ = 'staff'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    email = Column(String(100), unique=True, nullable=False)
    phone = Column(String(20))
    role = Column(String(50))
    position = Column(String(50))
    password = Column(String(255))
    status = Column(String(50), default='Active')
    created_at = Column(DateTime, default=datetime.utcnow)

class Branch(Base):
    __tablename__ = 'branches'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    location = Column(String(255))
    status = Column(String(50), default='Active')
    created_at = Column(DateTime, default=datetime.utcnow)

class Advertisement(Base):
    __tablename__ = 'advertisements'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    platform = Column(String(50))
    campaign = Column(String(100))
    status = Column(String(50), default='Active')
    created_at = Column(DateTime, default=datetime.utcnow)

# --- 3. PAGE ROUTES ---
@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        data = request.get_json()
        if data.get('email') == 'admin@origins.com' and data.get('password') == 'admin123':
            return jsonify({'success': True, 'redirect_url': '/admin/dashboard'})
        return jsonify({'success': False, 'message': 'Invalid credentials'})
    return render_template('login.html')

@app.route('/lead-form')
def lead_form():
    return render_template('lead_form.html')

@app.route('/admin/dashboard')
def admin_dashboard():
    return render_template('admin/base_layout.html')

@app.route('/staff/dashboard')
def staff_dashboard():
    return render_template('staff/staff_dashboard_module.html')

# --- 4. API ROUTES FOR SAVING DATA ---
@app.route('/api/save_staff', methods=['POST'])
def save_staff():
    data = request.form
    db_session = Session()
    try:
        new_staff = Staff(
            name=data.get('name'), email=data.get('email'), phone=data.get('phone'),
            role=data.get('role'), position=data.get('position'), 
            password=data.get('password'), status=data.get('status')
        )
        db_session.add(new_staff)
        db_session.commit()
        return jsonify({'success': True, 'message': 'Staff added successfully!'})
    except Exception as e:
        db_session.rollback()
        return jsonify({'success': False, 'message': str(e)})
    finally:
        db_session.close()

@app.route('/api/save_branch', methods=['POST'])
def save_branch():
    data = request.form
    db_session = Session()
    try:
        new_branch = Branch(
            name=data.get('name'), location=data.get('location'), status=data.get('status')
        )
        db_session.add(new_branch)
        db_session.commit()
        return jsonify({'success': True, 'message': 'Branch added successfully!'})
    except Exception as e:
        db_session.rollback()
        return jsonify({'success': False, 'message': str(e)})
    finally:
        db_session.close()

@app.route('/api/save_advertisement', methods=['POST'])
def save_advertisement():
    data = request.form
    db_session = Session()
    try:
        new_ad = Advertisement(
            name=data.get('name'), platform=data.get('platform'), 
            campaign=data.get('campaign'), status=data.get('status')
        )
        db_session.add(new_ad)
        db_session.commit()
        return jsonify({'success': True, 'message': 'Advertisement added successfully!'})
    except Exception as e:
        db_session.rollback()
        return jsonify({'success': False, 'message': str(e)})
    finally:
        db_session.close()
