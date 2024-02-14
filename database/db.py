import mysql.connector

def main():
    mydb = mysql.connector.connect(
        #host="212.132.69.137",
        #user="root",
        #password="example"

        host="192.168.0.112",
        user="",
        password=""
    )

    mycursor = mydb.cursor()

    mycursor.execute("CREATE DATABASE IF NOT EXISTS S7;")
    mycursor.execute("USE S7;")

    mycursor.execute("CREATE TABLE IF NOT EXISTS tblData(id INT AUTO_INCREMENT PRIMARY KEY, data_retrieved TIMESTAMP, energy_usage DOUBLE, machine_status varchar(255));")
    mycursor.execute("CREATE TABLE IF NOT EXISTS tblEnergyPrices(id INT AUTO_INCREMENT PRIMARY KEY, start_date TIMESTAMP, price DOUBLE);")

    mycursor.close()
    mydb.commit()
    mydb.close()

if __name__ == '__main__':
    main()