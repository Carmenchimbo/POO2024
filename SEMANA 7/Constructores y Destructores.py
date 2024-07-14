class Persona:
    def __init__(self, nombre, edad, direccion):
        """
        Constructor de la clase Persona.
        Inicializa los atributos nombre, edad y direccion.
        """
        self.nombre = nombre
        self.edad = edad
        self.direccion = direccion
        print(f"Persona creada: {self.nombre}, {self.edad} años, vive en {self.direccion}")

    def __del__(self):
        """
        Destructor de la clase Persona.
        Realiza tareas de limpieza cuando el objeto es destruido.
        """
        print(f"Persona eliminada: {self.nombre}")

# Creando una instancia de Persona
persona1 = Persona("Juan Pérez", 30, "Calle Falsa 123")

# Eliminando la referencia para llamar al destructor explícitamente
del persona1


class ConexionBaseDatos:
    def __init__(self, db_name):
        """
        Constructor de la clase ConexionBaseDatos.
        Inicializa y abre una conexión a una base de datos.
        """
        self.db_name = db_name
        self.conexion = self.abrir_conexion(db_name)
        print(f"Conexión a la base de datos '{self.db_name}' establecida.")

    def abrir_conexion(self, db_name):
        """
        Simula la apertura de una conexión a una base de datos.
        """
        # Aquí iría el código para abrir una conexión real.
        # Por simplicidad, solo retornamos un string.
        return f"Conexión a {db_name}"

    def cerrar_conexion(self):
        """
        Simula el cierre de una conexión a una base de datos.
        """
        # Aquí iría el código para cerrar una conexión real.
        print(f"Conexión a la base de datos '{self.db_name}' cerrada.")

    def __del__(self):
        """
        Destructor de la clase ConexionBaseDatos.
        Cierra la conexión a la base de datos.
        """
        self.cerrar_conexion()

# Creando una instancia de ConexionBaseDatos
conexion = ConexionBaseDatos("mi_base_de_datos")

# Eliminando la referencia para llamar al destructor explícitamente
del conexion
