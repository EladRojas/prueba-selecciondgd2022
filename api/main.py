
import requests
import json
import numpy as np

URL_API = "https://datos.gob.cl/api/3/action/datastore_search"
ID_API = "3d54e961-d81b-4507-aeee-7a433e00a9bf"

def getDatosAPI():
    data = requests.get(URL_API, params={"resource_id": ID_API})
    if data.status_code == 200:
        return data
    else:
        return print("Error al conectar con API....: " + data.status_code)

def listaEstaciones():
    dataAll = getDatosAPI().json()
    print("Resultado ->")
    for r in dataAll["result"]["records"]:
        print("ID: " + str(r["_id"]), "- Nombre Estación: " + r["NOMBRE FANTASIA"], "- Dirección: " + r["DIRECCION"], "- Comuna: " + r["COMUNA"], "- Línea: " + r["CODIGO"])
    print("-------------------------------------")
    print("")
    inicioProgram()


def filtraEstaciones(comuna, codigo):
    dataFilList = json.loads(getDatosAPI().text)
    recordsFilList = dataFilList["result"]["records"]
    fil = [x for x in recordsFilList if x['COMUNA'].upper() == comuna.upper() and x['CODIGO'].upper() == codigo.upper()]        
    print("Resultado ->")
    for f in fil:
        print("ID: " + str(f["_id"]),"- Nombre Estación: " + f["NOMBRE FANTASIA"], "- Dirección: " + f["DIRECCION"], "- Comuna: " + f["COMUNA"], "- Línea: " + f["CODIGO"])
    print("-------------------------------------")
    print("")
    inicioProgram()


def detEstacion(id):
    dataDetList = json.loads(getDatosAPI().text)
    recordsDetList = dataDetList["result"]["records"]
    det = [x for x in recordsDetList if x['_id'] == int(id)]
    print("Resultado ->")
    for d in det:
        print("Horarios: " + d["HORARIO REFERENCIAL"])
    print("-------------------------------------")
    print("")
    inicioProgram()


def listComunas():
    dataComunasList = json.loads(getDatosAPI().text)
    recordsComunasList = dataComunasList["result"]["records"]
    listComunas = []
    for n in recordsComunasList:
        listComunas.append(n["COMUNA"])
    comunasNp = np.array(listComunas)
    print(np.unique(comunasNp))
    print("-------------------------------------")
    print("")
    inicioProgram()


def listLineas():
    dataLineasList = json.loads(getDatosAPI().text)
    recordsLineasList = dataLineasList["result"]["records"]
    listLineas = []
    for n in recordsLineasList:
        listLineas.append(n["CODIGO"])
    lineasNp = np.array(listLineas)
    print("Resultado ->")
    print(np.unique(lineasNp))
    print("-------------------------------------")
    print("")
    inicioProgram()

def inicioProgram():
    print("Opción 1: - Listar Estaciones")
    print("Opción 2: - Filtrar Estaciones")
    print("Opción 3: - Detalle Estación")
    print("Opción 4: - Lista de Comunas")
    print("Opción 5: - Lista de Líneas de Metro")

    print("")
    opcionFuncion = input("Ingrese opción: ")
    print("")
    
    if opcionFuncion == "1":
        listaEstaciones()
    elif opcionFuncion == "2":
        comuna = input("Ingrese Nombre de Comuna: ")
        codigo = input("Ingrese Línea de Metro (ej: L1): ")
        if comuna == "" or codigo == "":
            print("Debe ingresar un Nombre de Comuna y Línea")
        else:
            filtraEstaciones(comuna,codigo)
    elif opcionFuncion == "3":
        id = input("Ingrese ID de Estación: ")
        if id.isnumeric():
            detEstacion(id)
        else:
            print("Debe ingresar un ID válido de Estación (El ID es un número entero")
    elif opcionFuncion == "4":
        listComunas()
    elif opcionFuncion == "5":
        listLineas()
    else:
        print("Opción inválida, debe ingresar 1, 2 o 3")


inicioProgram()

"""
print("Conectando a API....") 
data = requests.get("https://datos.gob.cl/api/3/action/datastore_search", params={"resource_id": "3d54e961-d81b-4507-aeee-7a433e00a9bf", "limit":25}) 

if data.status_code == 200:
    print("Obteniendo datos....") 
    data = data.json()
    
    print("Recorriendo datos....") 
    for rec in data["result"]["records"]:
        print(rec ["NOMBRE FANTASIA"])
        print(rec ["DIRECCION"])
        print(rec ["COMUNA"])
        print(rec ["CODIGO"])    
        
else:
    print("Eror conectar con API....")
    print(data.status_code)
"""