from servicios import *
from datetime import datetime
def registrar_cliente(datos):
    datos = dict(datos)
    cliente = {}
    cliente["nombre"] = input("Ingrese el nombre: ")
    while True:
        try:
            cliente["documento"] = int(input("Ingrese el documento: "))
            break
        except ValueError:
            print("Documento inválida. Por favor, ingrese un número válido.")
    
    
    while True:
        try:
            cliente["edad"] = int(input("Ingrese la edad: "))
            break
        except ValueError:
            print("Edad inválida. Por favor, ingrese un número válido.")
        
    cliente["direccion"] = input("Ingrese su dirección de residencia: ")
    cliente["telefono"] = input("Ingrese su número de teléfono: ")
    cliente["correo"] = input("Ingrese un correo de recuperación: ")

    while True:
        print("Ingrese el número para clasificar al cliente")
        print("(1) si el cliente es nuevo")
        print("(2) si el cliente es recurrente")
        print("(3) si el cliente es fiel")
        try:
            opc = int(input(" :"))
            if opc == 1:
                cliente["tipoc"] = "nuevo"
                break
            elif opc == 2:
                cliente["tipoc"] = "recurrente"
                break
            elif opc == 3:
                cliente["tipoc"] = "fiel"
                break
            else:
                print("Ingrese un valor válido")
        except ValueError:
            print("Opción inválida. Intente nuevamente.")

    datos["clientes"].append(cliente)
    print("¡Cliente registrado con éxito!")
    return datos
def eliminar_cliente(datos):
    datos = dict(datos)
    documento =int(input("Ingrese el documento del cliente: "))
    
    for i in range(len(datos["clientes"])):
        if datos["clientes"][i]["documento"] == documento:
            confirmacion=int(input("Esta seguro? (1)Para eliminar (2)Para cancelar:"))
            if confirmacion==1:
           
                datos["clientes"].pop(i)
                print("cliente eliminado!")
                return datos
            elif confirmacion==2:
                print ("Cancelado con exito")
                break
                   
    
    return datos


def actualizar_cliente(datos):
    datos = dict(datos)
    documento = int(input("Ingrese el documento del cliente a reemplazar: "))
    
    for i in range(len(datos["clientes"])):
        if datos["clientes"][i]["documento"] == documento:
            
            while True:
                print("¿Qué te gustaría cambiar?")
                print("(1) para modificar el nombre")
                print("(2) para modificar el documento")
                print("(3) para modificar la edad")
                print("(4) para modificar la dirección")
                print("(5) para modificar el teléfono")
                print("(6) para modificar el correo")
                print("(7) para modificar el tipo de cliente")
                print("(0) para salir")
                
                opc = input("Ingrese la opción: ")
                
                try:
                    if opc == "1":
                        datos["clientes"][i]["nombre"] = input("Ingrese el nuevo nombre: ")
                        print("¡Nombre actualizado con éxito!")
                        print("--------------------------------------")
                    elif opc == "2":
                        datos["clientes"][i]["documento"] = int(input("Ingrese el nuevo documento: "))
                        print("¡Documento actualizado con éxito!")
                        print("--------------------------------------")
                    elif opc == "3":
                        datos["clientes"][i]["edad"] = int(input("Ingrese la nueva edad: "))
                        print("¡Edad actualizada con éxito!")
                        print("--------------------------------------")
                    elif opc == "4":
                        datos["clientes"][i]["direccion"] = input("Ingrese la nueva dirección: ")
                        print("¡Dirección actualizada con éxito!")
                        print("--------------------------------------")
                    elif opc == "5":
                        datos["clientes"][i]["telefono"] = input("Ingrese el nuevo teléfono: ")
                        print("¡Teléfono actualizado con éxito!")
                        print("--------------------------------------")
                    elif opc == "6":
                        datos["clientes"][i]["correo"] = input("Ingrese el nuevo correo: ")
                        print("¡Correo actualizado con éxito!")
                        print("--------------------------------------")
                    elif opc == "7":
                        datos["clientes"][i]["tipoc"] = input("Ingrese el nuevo tipo de cliente: ")
                        print("¡Tipo de cliente actualizado con éxito!")
                        print("--------------------------------------")
                    elif opc == "0":
                        break
                    else:
                        print("Opción no válida. Intente nuevamente.")
                except ValueError:
                    print("Error: ¡Ingrese un valor válido!")
                    print("--------------------------------------")
                except Exception as e:
                    print("Error:", e)
    return datos


def factura(datos, datos2):
    datos = dict(datos)
    total = 0
    print("Bienvenido")

    print("------------------------------------------------")
    doc = int(input("Ingrese su número de documento: "))
    for cliente in datos["clientes"]:
        if cliente["documento"] == doc:
            print("¿Qué desea comprar?")
            while True:
                print(mostrar_catalogo(datos2))
                compra = input("Ingrese la referencia del producto a comprar: ")
                for producto in datos2["productos"]:
                    if compra == producto["ref"]:
                        try:
                            cant = int(input("¿Cuántas unidades desea llevar?: "))
                            total = cant * float(producto["precio"].replace(" COP", "").replace(".", "").replace(",", ".")) # Ajuste del formato del precio
                            print("El total a pagar es de:", total, "COP")
                            guardar_factura(cliente, producto, cant, total)
                            return "Compra exitosa"
                        except ValueError:
                            print("Error: Por favor, ingrese un número entero válido para la cantidad.")
                            continue
                print("Producto no encontrado. Intente nuevamente.")
            break
    return "No se ha encontrado el usuario ingresado"
def guardar_factura(cliente, producto, cantidad, total):
    factura_info = {
        "cliente": cliente["documento"],
        "producto": producto["ref"],
        "cantidad": cantidad,
        "total": total,
        "fecha_hora": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }
    try:
        with open("moduloventas.json", "r") as file:
            data = json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        data = []
    data.append(factura_info)
    with open("moduloventas.json", "w") as file:
        json.dump(data, file, indent=4)
        
        
