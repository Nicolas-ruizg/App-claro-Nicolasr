#imports
from datos import *
from menu import *
from clientes import *
from servicios import*

#Constants
RUTA_BASE_DE_DATOS = "clientes.json"
RUTA_BASE_DE_DATOS2 = "catalogo.json"





datos = cargar_datos(RUTA_BASE_DE_DATOS)
datos2 = cargar_datos(RUTA_BASE_DE_DATOS2)



while True:
    menu_principal()
    opc = pedir_opcion()
    if opc == 1:
        datos = registrar_cliente(datos)
    elif opc == 2:
        datos = eliminar_cliente(datos)
    elif opc == 3:
        datos = actualizar_cliente(datos)
    elif opc == 4:
        datos2 = registrar_servicio(datos2)
    elif opc == 5:
        datos2 = eliminar_servicio(datos2)
    elif opc == 6:
        datos2 = actualizar_servicio(datos2)
    elif opc == 7:
        datos3=mostrar_catalogo(datos2)
    elif opc == 8:
        print(factura(datos, datos2))
    elif opc == 9:
        productos_mas_vendidos()
    elif opc == 10:
        (datos)
    elif opc == 11:
        print("Salió!!")
        break
    else:
        print("Ingrese un valor valido")

guardar_datos(datos, RUTA_BASE_DE_DATOS)
guardar_datos(datos2, RUTA_BASE_DE_DATOS2)





