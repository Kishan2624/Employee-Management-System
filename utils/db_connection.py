# employee_management_system/utils/db_connection.py

import mysql.connector
from mysql.connector import Error
from config.db_config import DB_CONFIG


def create_connection():
    """
    Establishes a connection to the MySQL database using DB_CONFIG settings.
    Returns the connection object if successful, or None if there is an error.
    """
    try:
        connection = mysql.connector.connect(
            host=DB_CONFIG["host"],
            user=DB_CONFIG["user"],
            password=DB_CONFIG["password"],
            database=DB_CONFIG["database"]
        )
        if connection.is_connected():
            print("Connected to the database successfully.")
            return connection
    except Error as e:
        print(f"Error connecting to MySQL: {e}")
        return None


def close_connection(connection):
    """
    Closes the given MySQL database connection if it's open.
    """
    if connection and connection.is_connected():
        connection.close()
        print("Database connection closed.")
