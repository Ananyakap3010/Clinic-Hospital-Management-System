import mysql.connector

try:
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="Mris@1665",
        database="PATIENTS_DB"
    )
    print("Connected successfully!")
    conn.close()
except Exception as e:
    print("Failed to connect:", e)