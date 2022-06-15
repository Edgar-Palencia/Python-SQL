import csv 
import xlrd 
import os 
import psycopg2 
import django 
from yourapp import settings
django.setup() 
from yourapp import models 
 
 

 try: 
    conn = psycopg2.connect("Driver={SQL Server};SERVER={EDGAR\SQLEXPRESS};DATABASE={prueba1};UID={soporte};PWD={123}")
    cur = conn.cursor()


    filepath = 'D:\&Café\python-sql\data_ids.csv' 
    ext = os.path.splitext(filepath)[-1].lower()
    if (ext == '.csv'): 
        with open(filepath) as csvfile: 
        next(csvfile) 
        readCSV = csv.reader(csvfile, delimiter=',') 
        for row in readCSV: 
            print(row[1],row[1000]) 
            cur.execute("UPDATE inventario SET IDs = %s where id = %s", (row[1], row[1000])) 
            conn.commit() 
        conn.close()
        cur.close()
      
       except (Exception, psycopg2.DatabaseError) as error:
         print(error) 
         finally: if conn is not None:
          conn.close()

