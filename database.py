import psycopg2
from psycopg2.extras import DictCursor

# Database Configuration
DB_CONFIG = {
    "dbname": "ai_assistant",
    "user": "postgres",
    "password": "lebron@23",  # Replace with your actual password
    "host": "localhost",
    "port": "5432"
}

def get_db_connection():
    """Establishes a connection to PostgreSQL."""
    try:
        conn = psycopg2.connect(**DB_CONFIG)
        return conn
    except Exception as e:
        print("Database connection error:", e)
        return None

def get_leave_balance(user_id):
    """Fetches leave balance for a given user ID."""
    conn = get_db_connection()
    if not conn:
        return "Error: Cannot connect to database"

    try:
        cur = conn.cursor(cursor_factory=DictCursor)
        cur.execute("SELECT leave_balance FROM users WHERE id = %s", (user_id,))
        result = cur.fetchone()
        conn.close()
        return result["leave_balance"] if result else "User not found"
    except Exception as e:
        print("Error fetching leave balance:", e)
        return "Database query error"

def store_user_request(user_id, request_type, status):
    """Logs user requests into PostgreSQL."""
    conn = get_db_connection()
    if not conn:
        return "Error: Cannot connect to database"

    try:
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO user_requests (user_id, request_type, status) VALUES (%s, %s, %s)",
            (user_id, request_type, status),
        )
        conn.commit()
        conn.close()
        return "Request logged successfully"
    except Exception as e:
        print("Error logging user request:", e)
        return "Database insert error"
