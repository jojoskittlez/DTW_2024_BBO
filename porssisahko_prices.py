from datetime import datetime

import requests
import json
import mysql.connector


def db_connection():

    connection = mysql.connector.connect(
        host="212.132.69.137", #add docker container here
        user="root",
        password="example",
        database="S7"
    )

    cursor = connection.cursor()

    response = requests.get('https://api.porssisahko.net/v1/latest-prices.json')
    data = response.json()

    for entry in data['prices']:
        start_date_str = entry['startDate']
        price = entry['price']

        start_date = datetime.strptime(start_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        sql_query = "INSERT INTO tblEnergyPrices (start_date, price) VALUES (%s, %s);"
        cursor.execute(sql_query, (start_date, price))

    cursor.close()
    connection.commit()
    connection.close()


if __name__ == "__main__":
    db_connection()