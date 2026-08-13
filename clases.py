class Producto:
    def __init__(self,nombre,precio,cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        
    def sumar_cantidad(self,cantidad):
        self.cantidad += cantidad
        
    def restar_cantidad(self,cantidad):
        self.cantidad -= cantidad
        
    def mostrar_info(self):
        print(f"el nombre del producto es {self.nombre}")
        print(f"el precio del producto es {self.precio}")
        print(f"la cantidad del producto es {self.cantidad}")
    
    @staticmethod     
    def crear_producto():
        nombre = input("Digita el nombre del producto: ")
        precio = int(input("Digita el precio del producto: "))
        cantidad = int(input("Digita el cantidad del producto: "))
        return Producto(nombre, precio, cantidad)
    
    def __str__(self):
        return f"{self.nombre} - {self.precio} - {self.cantidad}"
    
    
class TipoProducto:
    def __init__(self,nombre):
        self.nombre = nombre
        
    