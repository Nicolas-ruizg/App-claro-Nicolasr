import json



def cargar_datos(archivo):
    datos = {}
    with open(archivo,"r") as file:
        datos=json.load(file)
    return datos
        
        

def guardar_datos(datos:dict, archivo):
    diccionario=json.dumps(datos, indent=4)
    file=open(archivo,"w")
    file.write(diccionario)
    file.close()
    
    
def generar_catalogo(archivo,mensaje):
    file = open(archivo,"w")
    file.write(mensaje)
    file.close()
    
def mostrar_catalogo_generado(archivo):
    with open(archivo) as catalogo:
        return catalogo.read()
    




    