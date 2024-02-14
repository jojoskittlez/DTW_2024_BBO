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
# namespace = "http://examples.freeopcua.github.io"


async def main():

    print(f"Connecting to {url} ...")
    async with Client(url=url) as client:
        # Find the namespace index
        #nsidx = await client.get_namespace_index(namespace)
        #print(f"Namespace Index for '{namespace}': {nsidx}")

        # Get the variable node for read / write
        #var = await client.nodes.root.get_children()
        #print(var)
        child_var = await client.nodes.objects.get_children()
        print(child_var)
        ref_var = await client.nodes.objects.get_references()
        print(ref_var)

        #for i in child_var:
        #    try:
        #        client.nodes.getvalue()
        #    except:
        #        print("idk man")

        #value = await var.read_value()
        #print(f"Value of MyVariable ({var}): {value}")

        #new_value = value - 50
        #print(f"Setting value of MyVariable to {new_value} ...")
        #await var.write_value(new_value)

        # Calling a method
        #res = await client.nodes.objects.call_method(f"{nsidx}:ServerMethod", 5)
        #print(f"Calling ServerMethod returned {res}")


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
            return True
    except Error as e:
        print(f"Error while connecting to MySQL: {e}")
        return False
    finally:
        # Close the database connection
        if connection.is_connected():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")


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
