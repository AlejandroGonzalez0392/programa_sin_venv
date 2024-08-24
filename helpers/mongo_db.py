URI = "Mensaje"

import pymongo

# Establecer conexión
URI = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = URI["calificaciones"] #Crea base de datos
