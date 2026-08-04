def agregar_elemento_a_lista(elemento,lista):
    if elemento:
        elemento = elemento.lower()
        lista.append(elemento)
        print("se agregó correctamente")
    else:
        print("El nombre del elemento no puede estar vacío")
    return lista 

def eliminar_producto_de_la_lista(indice_producto,lista):
    indice_producto = int(indice_producto)
    lista.pop(indice_producto)
    return lista 


def tipo_de_la_lista(tipo,lista):
    producto = tipo.lower()
    lista.append(tipo)
    return lista 

def listar_elementos(lista,nombre):
    print(f"La lista de {nombre} es: ")
    for indice,nombre_producto in enumerate(lista):
        print(indice,nombre_producto)

def relacionar_tipos_y_productos(tipos_productos,lista_productos,relacion_tipos_y_productos):
    listar_elementos(tipos_productos,"tipos de productos")
    indice_tipo_producto = int(input("selecciona el tipo de producto a relacionar: "))
    tipo_producto = tipos_productos[indice_tipo_producto]
    listar_elementos(lista_productos, "lista de productos")
    indice_producto = int(input("selecciona el producto a relacionar: "))
    producto = lista_productos[indice_producto]
    if tipo_producto in relacion_tipos_y_productos:
        relacion_tipos_y_productos[tipo_producto].append(producto)
    else:
        relacion_tipos_y_productos[tipo_producto] = [producto]