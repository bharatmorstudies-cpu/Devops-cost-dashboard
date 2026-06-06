# DevOps AWS Resource & Cost Dashboard

## Why We Are Performing This Project
Cloud costs can quickly grow out of control if left unmonitored. This project provides a centralized dashboard built specifically for **AWS** to track daily costs, isolate low-utilization resources, and pinpoint spending anomalies before they cause unexpected budget overruns.

## Architecture & Tech Stack
- **Frontend Dashboard:** React.js (To be built)
- **Backend API Layer:** Python FastAPI (To be built)
- **Database Engine:** Local PostgreSQL Server
- **Cloud Library:** AWS SDK for Python (`boto3`)

## Project Progress Track

### ✅ Sprint 1: Local Workspace Setup & Authentication
- Initialized project directory structure (`backend/` and `frontend/`).
- Connected securely to the AWS programmatic API layer via `boto3`.
- Tracked and verified connection parameters locally using automated Git workflows.

### ✅ Sprint 2: Database Initialization (Completed)
- Installed local relational database engines (**PostgreSQL**) on the development environment.
- Configured programmatic data validation using Python `SQLAlchemy` and database drivers (`psycopg2-binary`).
- Executed `init_db.py` to securely provision schema structures (`daily_costs` metadata tables) locally.

---

## How to Initialize and Run the Database Layer

### 1. Prerequisites
- Python 3.10+ installed on your computer.
- PostgreSQL Server active on port `5432`.

### 2. Table Creation
Navigate into your backend folder and execute the database schema initializer script:
```bash
cd backend
python init_db.py
```
*Expected Output:*
```text
Connecting to Local PostgreSQL database...
Creating 'daily_costs' table if it doesn't exist...
🚀 Local Database table created successfully!
```
