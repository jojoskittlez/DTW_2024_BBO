import os

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


async def main():

    print(f"Connecting to {url} ...")
    async with Client(url=url) as client:

        childs = await client.nodes.objects.get_children()
        print(childs)
        a = await childs[2].get_children()
        print(a)
        b = await a[0].get_children()
        print(b)
        c = await b[0].get_children()
        print(c)
        d = await c[0].get_children()
        print(d)
        e = await d[0].read_value()
        print(e)



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
    try:
        asyncio.run(main())
    except:
        data = {
            "status": "running",
            "engery": "10",
        }

        insert_into_database(host="localhost:3306", database="opcua_data", user="opcua_user", password="opcua_password",
                             table="test", data=data)
