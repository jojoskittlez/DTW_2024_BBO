import json
import os
from datetime import datetime

try:
    import asyncio
except ImportError:
    print("Die asyncio-Bibliothek ist nicht installiert. Installiere sie jetzt...")
    os.system('pip install asyncio')
    import asyncio

try:
    import asyncua
except ImportError:
    print("Die asyncua-Bibliothek ist nicht installiert. Installiere sie jetzt...")
    os.system('pip install asyncua')
    import asyncua

try:
    import mysql.connector
except ImportError:
    print("Die mysql.connector-Bibliothek ist nicht installiert. Installiere sie jetzt...")
    os.system('pip install mysql.connector')
    import mysql.connector

from asyncua import Client
from mysql.connector import Error


url = "opc.tcp://192.168.88.3:4840"


#async def main():
#
#    print(f"Connecting to {url} ...")
#    async with Client(url=url) as client:
#
#        childs = await client.nodes.objects.get_children()
#
#        counter_status = await childs[2].get_children()[0].get_children()[0].get_children()[0].get_children()[0].read_value()

def main():

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

    file_path = "..\\test_data\\machine_mock_data.json"

    with open(file_path, 'r') as file:
        json_data = file.read()

    data = json.loads(json_data)

    for val in data:
        data_retrieved_str = val['timestamp']
        energy_usage = val['energy_usage']
        machine_status = val['machine_status']

        data_retrieved = datetime.strptime(data_retrieved_str, "%Y-%m-%dT%H:%M:%S.%fZ")
        sql_query = "INSERT INTO tblData (data_retrieved, energy_usage, machine_status) VALUES (%s, %s, %s);"
        cursor.execute(sql_query, (data_retrieved, energy_usage, machine_status))

    cursor.close()
    connection.commit()
    connection.close()


def insert_into_database(host, database, user, password, table, data):
    try:
        # Connect to the database
        connection = mysql.connector.connect(host=host,
                                             database=database,
                                             user=user,
                                             password=password)
        if connection.is_connected():
            cursor = connection.cursor()

            # Create the insert query
            columns = ', '.join(data.keys())
            placeholders = ', '.join(['%s'] * len(data))
            query = f"INSERT INTO {table} ({columns}) VALUES ({placeholders})"

            # Execute the query
            cursor.execute(query, tuple(data.values()))

            # Commit the changes
            connection.commit()

            print(f"Data inserted successfully into {table} table.")
            # Close the database connection
            if connection.is_connected():
                cursor.close()
                connection.close()
                print("MySQL connection is closed.")
                return True
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return False



if __name__ == "__main__":
    #try:
        main()
    #except:
    #    data = {
    #        "status": "running",
    #        "energy": "10",
    #    }
#
    #    insert_into_database(host="localhost:3306", database="opcua_data", user="opcua_user", password="opcua_password",
    #                         table="test", data=data)
