import mysql.connector
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base

# 1. First, ensure the database 'origins_ivf' exists
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
    print(f"Error creating database: {e}")
    exit()

# 2. Use SQLAlchemy to define and create the Patient table
DATABASE_URL = "mysql+mysqlconnector://admin:OriginsIVF123.@origins-ivf-db.chmaic0ym2vl.ap-south-1.rds.amazonaws.com:3306/origins_ivf"

engine = create_engine(DATABASE_URL)
Base = declarative_base()

class Patient(Base):
    __tablename__ = 'patients'
    
    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    phone = Column(String(20))
    status = Column(String(50), default='New Inquiry')

# This single command tells SQLAlchemy to write the SQL and create the table
Base.metadata.create_all(engine)
print("SUCCESS: 'patients' table created in the database!")
