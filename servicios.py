from datos import*
import os
import datetime
from collections import Counter
def registrar_servicio (datos):
    datos = dict(datos)
    servicio={}
    plan=  int(input("digite (1) si el plan es postpago (2) si es prepago (3) si es un celular (4) plan hogar: "))  
    if plan==1:
        servicio["ref"]=input("Ingrese el numero de referencia del nuevo paquete: ")
        servicio["gb"]=input("Ingrese la cantidad de gb que contiene el servicio: ")+( "Gb")
        servicio["incluye"]=input("Ingrese lo que incluye el servicio: ")
        servicio["app"]=input("Ingrese las apps incluidas en el servicio: ")
        servicio["precio"]=input("Ingrese el precio del paquete: ")+(" COP")
        servicio["tipo"]="post pago"
    
        datos["productos"].append(servicio)
    elif plan==2:
        servicio["ref"]=input("Ingrese el numero de referencia del nuevo paquete: ")
        servicio["gb"]=input("Ingrese la cantidad de gb que contiene el servicio: ")+( "Gb")
        servicio["incluye"]=input("Ingrese lo que incluye el servicio: ")
        servicio["app"]=input("Ingrese las apps incluidas en el servicio: ")
        servicio["precio"]=input("Ingrese el precio del paquete: ")+(" COP")
        servicio["tipo "]="prepago"
        datos["productos"].append(servicio)
    elif plan==3:
        servicio["ref"]=input("Ingrese el numero de referencia del nuevo celular: ")
        servicio["modelo"]=input("Ingrese el modelo del nuevo celular: ")
        servicio["espacio"]=input("Ingrese el espacio del nuevo celular: ")+(" GB")
        servicio["ram"]=input("Ingrese la cantidad de ram que posee: ")
        servicio["camara"]=input("Ingrese los mega pixeles del nuevo celular: ")+(" MP")
        servicio["precio"]=input("Ingrese el precio del nuevo celular: ")+(" COP")
        servicio["tipo"]="tecnologia"
        datos["productos"].append(servicio)
    elif plan==4:
        servicio["ref"]=input("Ingrese el numero de referencia del nuevo plan de internet : ")
        servicio["tipo de internet"]=input("Ingrese el tipo de internet : ")
        servicio["gb"]=input("Ingrese la cantidad de gb que contiene el plan: ")+(" GB")
        servicio["capacidad de subida"]=input("Ingrese la capacidad de subida: ")+(" M/S")
        servicio["capacidad de bajada"]=input("Ingrese la capacidad de bajada : ")+(" M/S")
        servicio["precio"]=input("Ingrese el precio del nuevo servicio de internet: ")+(" COP")
        servicio["tipo"]="plan hogar"

        datos["productos"].append(servicio)
    print("plan registrado con éxito!")
    return datos
def eliminar_servicio(datos):
    datos = dict(datos)
    ref =input("Ingrese la referencia del producto o plan: ")
    for i in range(len(datos["productos"])):
        if datos["productos"][i]["ref"] == ref:
           
            datos["productos"].pop(i)
            print("plan eliminado!")
            return datos
           
    print("plan o paquete no encontrado")
    return datos
def actualizar_servicio(datos):
    datos=dict(datos)
    try:
        opc=int(input("Ingrese (1)para modificar un plan (2)para modificar un celular (3)internet: "))
        ref =int
        (input("Ingrese la referencia del paquete a modificar : "))
        
        for i in range(len(datos["productos"])):
            if datos["productos"][i]["ref"]== ref:
                    print("¿que te gustaria cambiar?")
                
                    
                    while True:
                        
                        
                        if opc==1:
                            print("(1) para modificar el numero de referencia: ")
                            print("(2) para modificar la cantidad de gb: ")
                            print("(3) para modificar lo que incluye el paquete : ")
                            print("(4) para modificar las apps incluidas: ")
                            print("(5) para modificar el precio del paquete: ")
                            print("(6) para modificar el tipo de plan: ")

                            print("(0) para salir ")
                            opc=input("ingrese la opcion: ")
                            
                        
                            
                            
                            if opc=="1":
                                datos["productos"][i]["ref"]= int(input("ingrese la nueva referencia: "))
                                print("se guardo con exito")
                                print("------------------------------------------------")

                                
                            elif opc== "2":    
                                datos["productos"][i]["gb"]=input("ingrese las nuevas gb: ")+(" GB")
                                print("se guardo con exito")
                                print("------------------------------------------------")

                            elif opc=="3":
                                datos["productos"][i]["incluye"]=input("ingrese lo nuevo que incluye: ")
                                print("se guardo con exito")
                                print("------------------------------------------------")
                                
                            elif opc=="4":
                                datos["productos"][i]["apps incluidas"]=input("ingrese las apps incluidas: ")
                                print("se guardo con exito")
                                print("------------------------------------------------")
                            elif opc=="5":
                                datos["productos"][i]["precio"]=input("ingrese el nuevo precio: ")+(" COP")
                                print("se guardo con exito")
                                print("------------------------------------------------")
                            elif opc=="6":
                                datos["productos"][i]["tipo de plan"]=input("ingrese el nuevo tipo de plan: ")
                                print("se guardo con exito")
                                print("------------------------------------------------")
                            elif opc=="0":
                                break
                        
                        elif opc==2:
                            print("(1) para modificar la referencia: ")
                            print("(2) para modificar el modelo: ")
                            print("(3) para modificar el espacio : ")
                            print("(4) para modificar la ram: ")
                            print("(5) para modificar la camara: ")
                            print("(6) para modificar el precio: ")
                            print("(7) para modificar el tipo de plan: ")
                            print("(0) para salir ")
                            opc=input("ingrese la opcion: ")
                            if opc=="1":
                                datos["productos"][i]["ref"]= int(input("ingrese la nueva referencia: "))
                                print("se guardo con exito")
                                print("------------------------------------------------")

                                
                            elif opc== "2":    
                                datos["productos"][i]["modelo"]=input("ingrese el nuevo modelo: ")
                                print("se guardo con exito")
                                print("------------------------------------------------")

                            elif opc=="3":
                                datos["productos"][i]["espacio"]=input("ingrese el nuevo espacio: ")+(" GB")
                                print("se guardo con exito")
                                print("------------------------------------------------")
                                
                            elif opc=="4":
                                datos["productos"][i]["ram"]=input("ingrese la nueva ram: ")
                                print("se guardo con exito")
                                print("------------------------------------------------")
                            elif opc=="5":
                                datos["productos"][i]["camara"]=input("ingrese la nueva camara: ")+(" MP")
                                print("se guardo con exito")
                                print("------------------------------------------------")
                            elif opc=="6":
                                datos["productos"][i]["precio"]=input("ingrese el nuevo precio: ")+(" COP")
                                print("se guardo con exito")
                                print("------------------------------------------------")
                            elif opc=="0":
                                break
                        elif opc==3:
                            print("(1) para modificar la referencia: ")
                            print("(2) para modificar el tipo de internet: ")
                            print("(3) para modificar las gb : ")
                            print("(4) para modificar la capacidad de subida: ")
                            print("(5) para modificar la capacidad de bajada: ")
                            print("(6) para modificar el precio: ")
                            print("(7) para modificar el tipo de plan: ")
                            
                            print("(0) para salir ")
                            opc=input("ingrese la opcion: ")
                            if opc=="1":
                                datos["productos"][i]["ref"]= int(input("ingrese la nueva referencia: "))
                                print("se guardo con exito")
                                print("------------------------------------------------")

                                
                            elif opc== "2":    
                                datos["productos"][i]["tipo de internet"]=input("ingrese el nuevo tipo de internet: ")
                                print("se guardo con exito")
                                print("------------------------------------------------")

                            elif opc=="3":
                                datos["productos"][i]["gb"]=input("ingrese las nuevas gb: ")+(" GB")
                                print("se guardo con exito")
                                print("------------------------------------------------")
                                
                            elif opc=="4":
                                datos["productos"][i]["capacidad de subida"]=input("ingrese la nueva capacidad de subida: ")+(" M/S")
                                print("se guardo con exito")
                                print("------------------------------------------------")
                            elif opc=="5":
                                datos["productos"][i]["apacidad de bajada"]=input("ingrese la nueva apacidad de bajada: ")+(" M/S")
                                print("se guardo con exito")
                                print("------------------------------------------------")
                            elif opc=="6":
                                datos["productos"][i]["precio"]=input("ingrese el nuevo precio: ")+(" COP")
                                print("se guardo con exito")
                                print("------------------------------------------------")
                            elif opc=="7":
                                datos["productos"][i]["tipo de plan"]=input("ingrese el nuevo tipo: ")
                                print("se guardo con exito")
                                print("------------------------------------------------")
                            elif opc=="0":
                                break
                                
                        break
    except Exception as e:
        print("Error:", e)
    return datos
def mostrar_catalogo(datos):
    datos = dict(datos)
    print("Bienvenido usuario")
    print("Ingrese (1) para mostrar los planes postpago")
    print("Ingrese (2) para mostrar los planes prepago")
    print("Ingrese (3) para mostrar electrodomésticos")
    print("Ingrese (4) para mostrar los planes de internet hogar")
    
    mensaje="No hay catalogo actual"
    
    opc = int(input("Ingrese qué tipo de plan quiere ver en pantalla: "))

    if opc == 1:  # Mostrar planes postpago
        print("Planes Postpago:")
        for productos in range(len(datos["productos"])):
            if datos["productos"][productos]["tipo"] == "post pago":
                print("-----------------------------")
                print("Referencia:",datos["productos"][productos]["ref"])
                print("Precio:", datos["productos"][productos]["precio"])
                print("Gigas:", datos["productos"][productos]["gb"])
                print("incluye:", datos["productos"][productos]["incluye"])
                print("Apps incluidas:", datos["productos"][productos]["app"])
                print("tipo de plan:",datos["productos"][productos]["tipo"])               
                print("-----------------------------")
                mensaje=""
               #
                print("-----------------------------")
        return mensaje
                

    elif opc == 2:  # Mostrar planes prepago
        print("Planes Prepago:")
        for productos in range(len(datos["productos"])):
            if datos["productos"][productos]["tipo"] == "prepago":
                print("-----------------------------")
                print("Referencia:",datos["productos"][productos]["ref"])
                print("Precio:", datos["productos"][productos]["precio"])
                print("Gigas:", datos["productos"][productos]["gb"])
                print("incluye:", datos["productos"][productos]["incluye"])
                print("Apps incluidas:", datos["productos"][productos]["app"])
                print("tipo de plan:",datos["productos"][productos]["tipo"])               
                print("-----------------------------")
                mensaje=""
                
        return mensaje          
                
    elif opc == 3:  # Mostrar electrodomésticos
        print("Electrodomésticos:")
        for productos in range(len(datos["productos"])):
            if datos["productos"][productos]["tipo"] == "tecnologia":
                print("-----------------------------")
                print("Referencia:",datos["productos"][productos]["ref"])
                print("Precio:", datos["productos"][productos]["precio"])
                print("incluye:", datos["productos"][productos]["modelo"])
                print("Apps incluidas:", datos["productos"][productos]["espacio"])
                print("Apps incluidas:", datos["productos"][productos]["ram"])
                print("Apps incluidas:", datos["productos"][productos]["camara"])
                print("tipo de plan:",datos["productos"][productos]["tipo"])               
                print("-----------------------------")
                mensaje=""
        return mensaje

    elif opc == 4:  # Mostrar planes de internet fija
        print("Planes de Internet Fija:")
        for productos in range(len(datos["productos"])):
            if datos["productos"][productos]["tipo"] == "plan hogar":
                print("-----------------------------")
                print("Referencia:",datos["productos"][productos]["ref"])
                print("Precio:", datos["productos"][productos]["precio"])
                print("Gigas:", datos["productos"][productos]["gb"])
                print("Capacidad de subida:", datos["productos"][productos]["capacidad de subida"])
                print("Capacidad de bajada:", datos["productos"][productos]["capacidad de bajada"])
                print("Tipo de internet:", datos["productos"][productos]["tipo de internet"])
                print("Tipo de plan:",datos["productos"][productos]["tipo"])               
                print("-----------------------------")
                mensaje=""
                
        return mensaje       

    else:
        return "COMPRA CANCELADA"
    
def productos_mas_vendidos():
    try:
        with open("moduloventas.json", "r") as file:
            data_ventas = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print("No hay datos de ventas disponibles.")
        return
    
    try:
        catalogo = cargar_datos("catalogo.json")
    except (FileNotFoundError, json.JSONDecodeError):
        print("No se puede cargar el catálogo de productos.")
        return
    
    productos_vendidos = Counter([factura["producto"] for factura in data_ventas])
    
    if not productos_vendidos:
        print("No se han vendido productos aún.")
        return
    
    print("Productos más vendidos:")
    for producto, cantidad in productos_vendidos.most_common():
        tipo_producto = next((item["tipo"] for item in catalogo["productos"] if item["ref"] == producto), None)
        if tipo_producto:
            print(f"Producto: {producto}, Tipo: {tipo_producto}, Cantidad vendida: {cantidad}")
        else:
            print(f"Producto: {producto}, Tipo: Desconocido, Cantidad vendida: {cantidad}")

