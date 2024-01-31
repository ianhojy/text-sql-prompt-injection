users_schema = """
    id INTEGER PRIMARY KEY,
    username TEXT NOT NULL,
    password TEXT NOT NULL
"""

transactions_schema = """
    transaction_id INTEGER PRIMARY KEY,
    user_id INTEGER,
    item TEXT NOT NULL,
    amount REAL NOT NULL,
    permission INTEGER,
    date TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES users(id)
"""
