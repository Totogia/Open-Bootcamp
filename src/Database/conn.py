import sqlite3

conn= sqlite3.connect ("D:\Microsoft VS Code\proyectos\proyectos\OpenBootcamp\python_conexion\src\Database\Base_de_datos_SQLite.db")
cursor = conn.cursor ()

#nombre_buscar = input ("¿Que primarca busca?")
rows = cursor.execute ("SELECT * FROM Primarcas WHERE Nombre ='Mortarion'")

Fila= cursor.fetchone ()

print ("  N°,   Nombre,    Planeta,    Region")
print (Fila) 

cursor.close ()
conn.close ()