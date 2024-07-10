# Clase que representa un vehículo en el concesionario
class Vehiculo:
    def __init__(self, id_vehiculo, marca, modelo, precio):
        self.id_vehiculo = id_vehiculo  # Identificador único del vehículo
        self.marca = marca  # Marca del vehículo
        self.modelo = modelo  # Modelo del vehículo
        self.precio = precio  # Precio del vehículo
        self.disponible = True  # Estado de disponibilidad del vehículo

    def vender(self):
        """Marca el vehículo como no disponible."""
        self.disponible = False

    def __str__(self):
        return f"{self.marca} {self.modelo} (ID: {self.id_vehiculo}) - {'Disponible' if self.disponible else 'Vendido'} - Precio: ${self.precio}"

# Clase que representa un cliente del concesionario
class Cliente:
    def __init__(self, id_cliente, nombre, email):
        self.id_cliente = id_cliente  # Identificador único del cliente
        self.nombre = nombre  # Nombre del cliente
        self.email = email  # Email del cliente

    def __str__(self):
        return f"Cliente {self.nombre} (ID: {self.id_cliente}) - Email: {self.email}"

# Clase que representa una venta de un vehículo a un cliente
class Venta:
    def __init__(self, vehiculo, cliente, fecha):
        self.vehiculo = vehiculo  # Vehículo vendido
        self.cliente = cliente  # Cliente que compró el vehículo
        self.fecha = fecha  # Fecha de la venta

    def __str__(self):
        return f"Venta: {self.vehiculo.marca} {self.vehiculo.modelo} a {self.cliente.nombre} el {self.fecha}"

# Clase que representa el concesionario
class Concesionario:
    def __init__(self, nombre):
        self.nombre = nombre  # Nombre del concesionario
        self.vehiculos = {}  # Diccionario de vehículos disponibles
        self.clientes = {}  # Diccionario de clientes registrados
        self.ventas = []  # Lista de ventas realizadas

    def agregar_vehiculo(self, vehiculo):
        """Agrega un vehículo al concesionario."""
        self.vehiculos[vehiculo.id_vehiculo] = vehiculo

    def registrar_cliente(self, cliente):
        """Registra un nuevo cliente en el concesionario."""
        self.clientes[cliente.id_cliente] = cliente

    def realizar_venta(self, id_vehiculo, id_cliente, fecha):
        """Realiza una venta de un vehículo a un cliente."""
        if id_vehiculo in self.vehiculos and id_cliente in self.clientes:
            vehiculo = self.vehiculos[id_vehiculo]
            cliente = self.clientes[id_cliente]
            if vehiculo.disponible:
                vehiculo.vender()
                venta = Venta(vehiculo, cliente, fecha)
                self.ventas.append(venta)
                return venta
            else:
                print("El vehículo no está disponible.")
                return None
        else:
            print("Vehículo o cliente no encontrado.")
            return None

    def listar_ventas(self):
        """Lista todas las ventas realizadas en el concesionario."""
        for venta in self.ventas:
            print(venta)

# Ejemplo de uso del sistema de gestión de vehículos en un concesionario

# Crear el concesionario
concesionario = Concesionario("Vehículos XYZ")

# Agregar vehículos al concesionario
vehiculo1 = Vehiculo(1, "Toyota", "Corolla", 18000)
vehiculo2 = Vehiculo(2, "Honda", "Civic", 22000)
vehiculo3 = Vehiculo(3, "Tesla", "Model 3", 35000)
concesionario.agregar_vehiculo(vehiculo1)
concesionario.agregar_vehiculo(vehiculo2)
concesionario.agregar_vehiculo(vehiculo3)

# Registrar clientes en el concesionario
cliente1 = Cliente(1, "Carlos Martínez", "carlos@example.com")
cliente2 = Cliente(2, "María López", "maria@example.com")
cliente3 = Cliente(3, "Pedro Sánchez", "pedro@example.com")
concesionario.registrar_cliente(cliente1)
concesionario.registrar_cliente(cliente2)
concesionario.registrar_cliente(cliente3)

# Realizar una venta
venta1 = concesionario.realizar_venta(1, 1, "2023-05-15")
venta2 = concesionario.realizar_venta(3, 2, "2023-06-20")

# Listar todas las ventas
print("\nVentas realizadas:")
concesionario.listar_ventas()

# Listar el estado de los vehículos
print("\nEstado de los vehículos:")
for vehiculo in concesionario.vehiculos.values():
    print(vehiculo)