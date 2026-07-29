from funciones_menu import *

lista_productos = []


while True:
    print('--------------------------------')
    print('Menú')
    print('--------------------------------')
    print('Opción 1: Añadir Productos: ')
    print('Opción 2: Eliminar Productos: ')
    print('Opción 3: Añadir Tipos De Productos: ')
    print('Opción 4: Listar Productos: ')
    print('Opción 5: Verificar Existencia De Productos: ')
    print('--------------------------------')

    solicitud_info = input('Coloca la opción que desees: ')
    
    match solicitud_info:
        case "1": 
            producto_nuevo = input("Digita tu producto: ")
            agregar_producto_a_lista(producto_nuevo,lista_productos)
        case "2":
            eliminar_producto = input("Digita tu producto: ")
            eliminar_producto_de_la_lista(eliminar_producto,lista_productos)
            print(f"se eliminó correctamente {lista_productos}")
        case "3":
            print('Usted ha elegido la opción 3')
        case "4":
            listar_productos(lista_productos)
        case _:
            print("Usted no ha seleccionado una opción válida")
            
