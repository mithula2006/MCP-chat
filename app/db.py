import psycopg2

DB_CONFIG = {
    "dbname": "policy_db",
    "user": "postgres",
    "password": "Simk@123",
    "host": "localhost",
    "port": 5432
}

def get_connection():
    return psycopg2.connect(**DB_CONFIG)
