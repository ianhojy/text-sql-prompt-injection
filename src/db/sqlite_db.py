
import sqlite3
from src.db.schema import transactions_schema, users_schema

def execute_sql(sql_query):
    conn = sqlite3.connect('../temp_db/example.db')
    cursor = conn.cursor()
    cursor.execute(sql_query)
    return cursor.fetchall()

def reset_database():
    
    conn = sqlite3.connect('../temp_db/example.db')
    cursor = conn.cursor()
    cursor.execute('DROP TABLE IF EXISTS users')
    cursor.execute(f'''
        CREATE TABLE users (
            {users_schema}
        )
    ''')
    cursor.execute('DROP TABLE IF EXISTS transactions')
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS transactions (
            {transactions_schema}
        )
    ''')


    users = [
        (1, 'Alice', 'password123'),
        (2, 'Bob', 'qwerty'),
        (3, 'Charlie', 'asdfgh'),
        (4, 'David', '123456'),
        (5, 'Eve', 'passw0rd')
    ]

    cursor.executemany('INSERT INTO users VALUES (?, ?, ?)', users)
    transactions = [
        (1, 1, 'Laptop', 1200.00, 1),
        (2, 3, 'Headphones', 1300.00, 0),
        (3, 2, 'Smartphone', 800.00, 1),
        (4, 3, 'Book', 20.00, 0),
        (5, 2, 'Tablet', 400.00, 1),
        (6, 4, 'Monitor', 300.00, 1),
        (7, 5, 'Keyboard', 100.00, 0),
        (8, 1, 'Mouse', 25.00, 1),
        (9, 2, 'Webcam', 90.00, 0),
        (10, 3, 'Desk Lamp', 45.00, 1),
        (11, 4, 'Charger', 35.00, 0),
        (12, 5, 'Backpack', 60.00, 0),
        (13, 1, 'External Hard Drive', 120.00, 1),
        (14, 2, 'Printer', 200.00, 1),
        (15, 3, 'Speakers', 85.00, 0),
        (16, 4, 'USB Hub', 30.00, 0),
        (17, 5, 'Office Chair', 250.00, 0),
        (18, 1, 'Notebook', 10.00, 0),
        (19, 2, 'Pen Drive', 50.00, 0),
        (20, 3, 'Router', 150.00, 0)
    ]
    cursor.executemany('INSERT INTO transactions (transaction_id, user_id, item, amount, permission) VALUES (?, ?, ?, ?, ?)', transactions)
    conn.commit()
    conn.close()