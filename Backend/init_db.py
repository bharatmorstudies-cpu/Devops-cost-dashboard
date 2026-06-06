import os
from sqlalchemy import create_engine, Column, String, Float, Date
from sqlalchemy.orm import declarative_base

# 1. Configuration pointed to your own local computer
DB_USER = "postgres"
DB_PASSWORD = "bharat123"      # Change this if you chose a different password during installation
DB_HOST = "127.0.0.1"            # Points to your local laptop
DB_PORT = "5432"
DB_NAME = "postgres"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

# 2. Define the Table Structure
Base = declarative_base()

class DailyCost(Base):
    __tablename__ = 'daily_costs'
    
    date = Column(Date, primary_key=True)
    service_name = Column(String, primary_key=True)
    cost = Column(Float, nullable=False)
    currency = Column(String, default="USD")

# 3. Create the table locally
def initialize_database():
    print("Connecting to Local PostgreSQL database...")
    try:
        engine = create_engine(DATABASE_URL)
        print("Creating 'daily_costs' table if it doesn't exist...")
        Base.metadata.create_all(engine)
        print("🚀 Local Database table created successfully!")
    except Exception as e:
        print(f"❌ Error connecting to your local database: {e}")

if __name__ == "__main__":
    initialize_database()
