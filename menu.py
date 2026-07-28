while True:
    print('--------------------------------')
    print('Menú')
    print('--------------------------------')
    print('Opción 1: Añadir Productos: ')
    print('Opción 2: Eliminar Productos: ')
    print('Opción 3: Añadir Tipos De Productos: ')
    print('Opción 4: Listar Productos: ')
    print('--------------------------------')

    solicitud_info = input('Coloca la opción que desees: ')
    
    match solicitud_info:
        case "1": 
            print('Usted ha elegido la opción 1')
        case "2":
            print('Usted ha elegido la opción 2')
        case "3":
            print('Usted ha elegido la opción 3')
        case "4":
            print('Usted ha elegido la opción 4')
        case _:
            print("Usted no ha seleccionado una opción válida")    