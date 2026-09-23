import sqlite3#I need python's built in SQLite tools.

# =================================
# Connect to the WeServe database
# =================================

connection = sqlite3.connect("weserve.db")#Connecting my python program to the database

# Create a cursor to execute SQL commands on the db
cursor = connection.cursor()

# ========================================
# Create the users table
# ========================================

cursor.execute("""
    CREATE TABLE users (
        id INTEGER PRIMARY KEY,
        first_name TEXT,
        second_name TEXT,
        email TEXT,
        password TEXT,
        gender TEXT
    )
""")