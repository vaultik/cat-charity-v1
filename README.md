# QRKot — Cat Charity Fund
 
A donation platform for cat support projects. Donations are automatically allocated to projects using a FIFO queue.  
Built with FastAPI + SQLAlchemy + Alembic.
 
> **This is v1** — core donation logic only.  
> [v2](https://github.com/Marakes/cat-charity-v2) adds user authentication (FastAPI Users).  
> [v3](https://github.com/Marakes/cat-charity-v3) adds Google Sheets export.
 
## Features
 
- Create charity projects with a fundraising target
- Make donations — automatically invested into open projects (oldest first, FIFO)
- Track investment progress per project and per donation
- Pytest test suite

## Tech Stack

- **Python 3.9**
- **FastAPI 0.111.0**
- **SQLAlchemy 2.0.29**
- **Alembic 1.7.7**
- **Pydantic 2.7.1**
- **pytest 7.1.3**

Full list of dependencies: `requirements.txt`
 
## How to Run
 
```bash
# Clone the repository
git clone https://github.com/Marakes/cat-charity-v1
cd cat-charity-v1
 
# Create and activate virtual environment
python3 -m venv venv
source venv/bin/activate        # Windows: venv\Scripts\activate
 
# Install dependencies
pip install --upgrade pip
pip install -r requirements.txt
 
# Apply migrations
alembic upgrade head
 
# Start the server
uvicorn app.main:app --reload
```
 
API docs available at `http://127.0.0.1:8000/docs`
 
## API Examples
 
**POST** `/charity_project/` — create a project
 
```json
// Request body
{
  "name": "WowWow",
  "description": "Needs more",
  "full_amount": 1000
}
 
// Response 200
{
  "name": "WowWow",
  "description": "Needs more",
  "full_amount": 1000,
  "id": 3,
  "invested_amount": 0,
  "fully_invested": false,
  "create_date": "2025-12-19T17:21:24.032248"
}
```
 
**GET** `/donation/` — list all donations
 
```json
[
  {
    "full_amount": 100,
    "comment": "string",
    "id": 1,
    "create_date": "2025-12-19T16:43:21.311806",
    "invested_amount": 100,
    "fully_invested": true,
    "close_date": "2025-12-19T16:43:21.322164"
  }
]
```
 
## Author
 
[github.com/Marakes](https://github.com/Marakes)
