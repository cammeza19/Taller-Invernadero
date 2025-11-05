import mysql.connector

def conectar():
    try:
        conexion = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="greengrowth"
        )
        return conexion
    except mysql.connector.Error as e:
        print("Error en la conexión:", e)
        return None
