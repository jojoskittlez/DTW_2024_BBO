import requests
import json
import mysql.connector

# request prices
response = requests.get('https://api.porssisahko.net/v1/latest-prices.json')
results = response.json()


def db_connection():

# Establish a connection to the database
    connection = mysql.connector.connect(
        host="127.0.0.1", #add docker container here
        user="opcua_user",
        password="opcua_password",
        database="opcua_data"
    )

    # Creating a cursor object to execute SQL queries
    cursor = connection.cursor()

    # Define your SQL query to insert data into your MariaDB table
    # Replace 'your_table' and 'your_column' with your actual table and column names
    sql_query = "INSERT INTO your_table (your_column) VALUES (%s)"

    # Loop through the JSON data and insert it into the database
    for key, value in results.items():
        cursor.execute(sql_query, (json.dumps(value),))

    # Commit the changes to the database
    connection.commit()

    # Close the cursor and connection
    cursor.close()
    connection.close()


if __name__ == "__main__":
    db_connection()