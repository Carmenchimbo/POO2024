import json

class Producto:
    def __init__(self, id, nombre, cantidad, precio):
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

    def establecer_cantidad(self, cantidad):
        self.cantidad = cantidad

    def obtener_precio(self):
        return self.precio

    def establecer_precio(self, precio):
        self.precio = precio

    def __str__(self):
        return f"ID: {self.id}, Nombre: {self.nombre}, Cantidad: {self.cantidad}, Precio: {self.precio}"

class Inventario:
    def __init__(self):
        self.productos = {}

    def añadir_producto(self, producto):
        if producto.obtener_id() in self.productos:
            print("Producto ya existe en el inventario.")
        else:
            self.productos[producto.obtener_id()] = producto
            print("Producto añadido correctamente.")

    def eliminar_producto(self, id):
        if id in self.productos:
            del self.productos[id]
            print("Producto eliminado correctamente.")
        else:
            print("Producto no encontrado en el inventario.")

    def actualizar_producto(self, id, cantidad=None, precio=None):
        if id in self.productos:
            if cantidad is not None:
                self.productos[id].establecer_cantidad(cantidad)
            if precio is not None:
                self.productos[id].establecer_precio(precio)
            print("Producto actualizado correctamente.")
        else:
            print("Producto no encontrado en el inventario.")

    def buscar_producto_por_nombre(self, nombre):
        resultados = [p for p in self.productos.values() if nombre.lower() in p.obtener_nombre().lower()]
        if resultados:
            for producto in resultados:
                print(producto)
        else:
            print("No se encontraron productos que coincidan con la búsqueda.")

    def mostrar_todos_los_productos(self):
        if not self.productos:
            print("El inventario está vacío.")
        else:
            for producto in self.productos.values():
                print(producto)

    def guardar_en_archivo(self, nombre_archivo):
        with open(nombre_archivo, 'w') as archivo:
            json.dump({id_producto: vars(producto) for id_producto, producto in self.productos.items()}, archivo)
        print(f"Inventario guardado en {nombre_archivo}.")

    def cargar_desde_archivo(self, nombre_archivo):
        try:
            with open(nombre_archivo, 'r') as archivo:
                datos = json.load(archivo)
                self.productos = {id_producto: Producto(**info) for id_producto, info in datos.items()}
            print(f"Inventario cargado desde {nombre_archivo}.")
        except FileNotFoundError:
            print(f"El archivo {nombre_archivo} no existe.")
        except json.JSONDecodeError:
            print("El archivo está vacío o tiene un formato incorrecto.")

def mostrar_menu():
    print("\n--- Menú del Inventario ---")
    print("1. Añadir producto")
    print("2. Eliminar producto")
    print("3. Actualizar cantidad de un producto")
    print("4. Actualizar precio de un producto")
    print("5. Buscar producto por nombre")
    print("6. Mostrar todos los productos")
    print("7. Guardar inventario en archivo")
    print("8. Cargar inventario desde archivo")
    print("9. Salir")

def main():
    inventario = Inventario()

    while True:
        mostrar_menu()
        opcion = input("Selecciona una opción: ")

        if opcion == '1':
            id = input("Ingresa el ID del producto: ")
            nombre = input("Ingresa el nombre del producto: ")
            try:
                cantidad = int(input("Ingresa la cantidad del producto: "))
            except ValueError:
                print("Por favor, ingresa un número entero válido para la cantidad.")
                continue
            try:
                precio = float(input("Ingresa el precio del producto: "))
            except ValueError:
                print("Por favor, ingresa un precio válido.")
                continue

            producto = Producto(id, nombre, cantidad, precio)
            inventario.añadir_producto(producto)

        elif opcion == '2':
            id = input("Ingresa el ID del producto a eliminar: ")
            inventario.eliminar_producto(id)

        elif opcion == '3':
            id = input("Ingresa el ID del producto: ")
            try:
                cantidad = int(input("Ingresa la nueva cantidad: "))
            except ValueError:
                print("Por favor, ingresa un número entero válido para la cantidad.")
                continue
            inventario.actualizar_producto(id, cantidad=cantidad)

        elif opcion == '4':
            id = input("Ingresa el ID del producto: ")
            try:
                precio = float(input("Ingresa el nuevo precio: "))
            except ValueError:
                print("Por favor, ingresa un precio válido.")
                continue
            inventario.actualizar_producto(id, precio=precio)

        elif opcion == '5':
            nombre = input("Ingresa el nombre del producto: ")
            inventario.buscar_producto_por_nombre(nombre)

        elif opcion == '6':
            inventario.mostrar_todos_los_productos()

        elif opcion == '7':
            nombre_archivo = input("Ingresa el nombre del archivo para guardar: ")
            inventario.guardar_en_archivo(nombre_archivo)

        elif opcion == '8':
            nombre_archivo = input("Ingresa el nombre del archivo para cargar: ")
            inventario.cargar_desde_archivo(nombre_archivo)

        elif opcion == '9':
            print("Saliendo del programa...")
            break

        else:
            print("Opción no válida. Por favor, intenta de nuevo.")

if __name__ == "__main__":
    main()
