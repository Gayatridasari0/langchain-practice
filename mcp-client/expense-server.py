from fastmcp import FastMCP
from datetime import datetime

app = FastMCP("expense-server")

EXPENSES = [
    {"date": "2024-11-01", "category": "Food", "amount": 25.50}, 
    {"date": "2024-11-03", "category": "Transport", "amount": 12.00}, 
    {"date": "2024-11-10", "category": "Groceries", "amount": 80.00}, 
    {"date": "2024-11-15", "category": "Shopping", "amount": 150.00}, 
    {"date": "2024-11-28", "category": "Food", "amount": 30.00},
]

def parse_date(s:str):
    return datetime.strptime(s, "%Y-%m-%d")

@app.tool()
def get_expenses(start_date: str, end_date: str) -> dict:
    """ 
    Return all expenses between start_date and end_date (inclusive).
    Dates must be in YYYY-MM-DD format.
    """
    start = parse_date(start_date)
    end = parse_date(end_date)

    filtered = [
        e for e in EXPENSES
        if start <= parse_date(e["date"]) <= end
    ]

    return {'expenses': filtered}

if __name__ == '__main__':
    app.run()