def agregar_producto_a_lista(producto,lista):
    if producto:
        producto = producto.lower()
        lista.append(producto)
        print("se agregó correctamente")
    else:
        print("El nombre del producto no puede estar vacío")
    return lista 

def eliminar_producto_de_la_lista(producto,lista):
    producto = producto.lower()
    lista.pop(producto)
    return lista 


def tipo_de_la_lista(tipo,lista):
    producto = tipo.lower()
    lista.append(tipo)
    return lista 

def listar_productos(lista):
    print("La lista de productos es: ")
    for indice,nombre_producto in enumerate(lista):
        print(indice,nombre_producto)