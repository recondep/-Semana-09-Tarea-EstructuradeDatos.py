
# producto.py

class Producto:
    def _init_(self, id, nombre, cantidad, precio):
        self.id = id
        self.nombre = nombre
        self.cantidad = cantidad
        self.precio = precio

    def obtener_id(self):
        return self.id

    def obtener_nombre(self):
        return self.nombre

    def obtener_cantidad(self):
        return self.cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def establecer_precio(self, precio):
        self.precio = precio

# inventario.py

from producto import Producto

class Inventario:
    def _init_(self):
        self.productos = []

    def agregar_producto(self, producto):
        """Agrega un producto al inventario."""
        if any(p.obtener_id() == producto.obtener_id() for p in self.productos):
            raise ValueError("Error: El ID del producto ya existe en el inventario.")
        self.productos.append(producto)

    def eliminar_producto(self, id):
        """Elimina un producto del inventario por su ID."""
        for p in self.productos:
            if p.obtener_id() == id:
                self.productos.remove(p)
                return
        raise ValueError("Error: Producto no encontrado en el inventario.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        """Actualiza la cantidad y/o precio de un producto en el inventario por su ID."""
        for p in self.productos:
            if p.obtener_id() == id:
                if cantidad is not None:
                    p.establecer_cantidad(cantidad)
                if precio is not None:
                    p.establecer_precio(precio)
                return
        raise ValueError("Error: Producto no encontrado en el inventario.")

    def buscar_producto_por_nombre(self, nombre):
        """Busca productos en el inventario por su nombre."""
        resultados = [p for p in self.productos if nombre.lower() in p.obtener_nombre().lower()]
        return resultados

    def mostrar_productos(self):
        """Muestra todos los productos en el inventario."""
        for p in self.productos:
            print(f"ID: {p.obtener_id()}, Nombre: {p.obtener_nombre()}, Cantidad: {p.obtener_cantidad()}, Precio: {p.obtener_precio()}")
