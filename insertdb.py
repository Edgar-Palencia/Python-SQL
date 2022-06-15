import csv
import sqlite3


archivo = open("D:\&Café\python-sql\data_ids.csv")

filas   = csv.reader(archivo,delimiter=";")

lista = list (filas)
del (lista[0])
tuplaa = tuple(lista)

#insertar

conexion = sqlite3.connect("inventario.db")
cursor   = conexion.cursor()
cursor.executemany("INSERT INTO inventario ('Ids') VALUES (?)",tuplaa)

conexion.commit()
conexion.close()