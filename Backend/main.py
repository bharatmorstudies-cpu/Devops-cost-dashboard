from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from sqlalchemy import create_engine, text

app = FastAPI(title="AWS Cost Optimization Dashboard API")

# Allow your Frontend folder to safely request data
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configuration pointing to your local PostgreSQL setup
DB_USER = "postgres"
DB_PASSWORD = "password123"  # Make sure this matches your database password!
DB_HOST = "127.0.0.1"
DB_PORT = "5432"
DB_NAME = "postgres"

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
engine = create_engine(DATABASE_URL)

@app.get("/")
def read_root():
    return {
        "status": "Online",
        "project": "DevOps Cost Dashboard API",
        "message": "Welcome! Your backend server is officially working."
    }

@app.get("/api/v1/costs")
def get_dashboard_costs():
    try:
        # Fetch actual stored entries from your database table
        with engine.connect() as connection:
            result = connection.execute(text("SELECT date, service_name, cost, currency FROM daily_costs ORDER BY date DESC"))
            
            costs_list = []
            for row in result:
                costs_list.append({
                    "date": str(row[0]),
                    "service": row[1],
                    "cost": row[2],
                    "currency": row[3]
                })
                
        return {"success": True, "data": costs_list}
    except Exception as e:
        return {"success": False, "error": str(e)}
