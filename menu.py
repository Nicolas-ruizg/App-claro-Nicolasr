def menu_principal():
    print("***************************************")
    print("Ingrese la opción que requiera")
    print("1. para registrar un cliente")
    print("2. para eliminar un cliente")
    print("3. para actualizar un cliente")
    print("4. para registrar un nuevo plan")
    print("5. para eliminar un plan")
    print("6. para actualizar un plan ")
    print("7. para mostrar el catalogo ")
    print("8. para comprar un producto ")
    print("9. para mostrar los productos mas vendidos")
    print("10. para ")
    print("11. para salir")
    print("***************************************")
    
def pedir_opcion():
    opc = 0
    try:
        opc = int(input("Ingrese su opción: "))
        print("***************************************")
        return opc
    except Exception:
        print("Valor inválido")
        print("***************************************")
        return -1