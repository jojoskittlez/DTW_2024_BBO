from datetime import datetime

import requests
import json
import mysql.connector


def db_connection():

    connection = mysql.connector.connect(
        host="212.132.69.137",
        user="root",
        password="example",

        #host="192.168.0.112",
        #user="pi",
        #password="123456789",
        database="S7"
    )

    cursor = connection.cursor()

    response = requests.get('https://api.porssisahko.net/v1/latest-prices.json')
    data = response.json()

    for val in data['prices']:
        start_date_str = val['startDate']
        price = val['price']

        start_date = datetime.strptime(start_date_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        sql_query = "INSERT INTO tblEnergyPrices (start_date, price) VALUES (%s, %s);"
        cursor.execute(sql_query, (start_date, price))

    cursor.close()
    connection.commit()
    connection.close()


if __name__ == "__main__":
    db_connection()