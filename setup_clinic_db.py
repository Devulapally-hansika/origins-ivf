import mysql.connector
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base
from datetime import datetime

# 1. Ensure the database 'origins_ivf' exists
try:
    conn = mysql.connector.connect(
        host='origins-ivf-db.chmaic0ym2vl.ap-south-1.rds.amazonaws.com',
        user='admin',
        password='OriginsIVF123.',
        port=3306
    )
    cursor = conn.cursor()
    cursor.execute("CREATE DATABASE IF NOT EXISTS origins_ivf")
    print("Database 'origins_ivf' is ready.")
    cursor.close()
    conn.close()
except Exception as e:
    print(f"Error connecting to database: {e}")
    exit()

# 2. Define the database connection URL
DATABASE_URL = "mysql+mysqlconnector://admin:OriginsIVF123.@origins-ivf-db.chmaic0ym2vl.ap-south-1.rds.amazonaws.com:3306/origins_ivf"
engine = create_engine(DATABASE_URL)
Base = declarative_base()

# --- TABLE DEFINITIONS ---

class Patient(Base):
    __tablename__ = 'patients'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20))
    status = Column(String(50), default='New Inquiry')

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

class DropdownCategory(Base):
    __tablename__ = 'dropdown_categories'
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False, unique=True)

class DropdownOption(Base):
    __tablename__ = 'dropdown_options'
    id = Column(Integer, primary_key=True)
    category_id = Column(Integer, nullable=False)
    name = Column(String(100), nullable=False)
    status = Column(String(50), default='Active')

# 3. Create all tables in the database
Base.metadata.create_all(engine)
print("SUCCESS: All tables are ready in the database!")
