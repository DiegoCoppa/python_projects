# -*- coding: utf-8 -*-

"""
import mysql.connector
from mysql.connector import errorcode

def mysqlrequest():
    try:cnx = mysql.connector.connect(user='diego', password='rojo666',
                              host='127.0.0.1',
                              database='dccCertificados')
    
    except mysql.connector.Error as err:
        if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
            print("Something is wrong with your user name or password")
        elif err.errno == errorcode.ER_BAD_DB_ERROR:
            print("Database does not exist")
        else:
            print(err)
    
    SELECT * FROM books
    ccnx.query()
    
    
    cnx.close()
    
    
    #SHOW DATABASES;
    
"""