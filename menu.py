from funciones_menu import *

lista_productos = []
tipos_productos = []
relacion_tipos_y_productos = {}

while True:
    print('--------------------------------')
    print('Menú')
    print('--------------------------------')
    print('Opción 1: Añadir Productos: ')
    print('Opción 2: Eliminar Productos: ')
    print('Opción 3: Añadir Tipos De Productos: ')
    print('Opción 4: Listar Productos: ')
    print('Opción 5: Verificar Existencia De Productos: ')
    print('Opción 6: Relacionar tipos y productos: ')
    print('Opción 7: Ver relacion entre tipos y productos: ')
    print('--------------------------------')

    solicitud_info = input('Coloca la opción que desees: ')
    
    match solicitud_info:
        case "1": 
            producto_nuevo = Producto.crear_producto()
            agregar_elemento_a_lista(producto_nuevo,lista_productos)
        case "2":
            listar_elementos(lista_productos,"productos")
            eliminar_producto = input("Digita el producto que deseas eliminar: ")
            eliminar_producto_de_la_lista(eliminar_producto,lista_productos)
            print(f"ahora la lista es {lista_productos}")
        case "3":
            tipo_producto_nuevo = TipoProducto.crear_tipo_producto()
            agregar_elemento_a_lista(tipo_producto_nuevo,tipos_productos)
        case "4":
            listar_elementos(lista_productos,"productos")
        case "6":
            relacionar_tipos_y_productos(tipos_productos, lista_productos, relacion_tipos_y_productos)
            print(relacion_tipos_y_productos)
        case _:
            print("Usted no ha seleccionado una opción válida")