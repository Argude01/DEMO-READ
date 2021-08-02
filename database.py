from codecs import register
import re
import mysql.connector

nombre = ""

class MyDatabase:
    def open_connection(self):
        connection = mysql.connector.connect( 
            host="localhost",                    
            user="root", 
            passwd="", 
            database="db_demo")
        return connection

    def read_db(self):
        my_connection = self.open_connection()
        cursor = my_connection.cursor()
        query = "SELECT * FROM TBL_USUARIOS WHERE ID_USUARIO = 1"
        cursor.execute(query)  
        for fila in cursor:
            nombre = fila[1]
            print("FILA - BackEnd: " + str(fila[1])) 
            print("RESULTADO - BackEnd: " + str(nombre))
        my_connection.close()     
