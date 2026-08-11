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
    
        
        
        

producto_1 = Producto("Manzana",1000,10)
producto_1.sumar_cantidad(15)
producto_1.restar_cantidad(7)
producto_1.mostrar_info()



