import sqlite3#I need python's built in SQLite tools.

# =================================
# Connect to the WeServe database
# =================================

connection = sqlite3.connect("weserve.db")#Connecting my python program to the database

# Create a cursor to execute SQL commands
cursor = connection.cursor()