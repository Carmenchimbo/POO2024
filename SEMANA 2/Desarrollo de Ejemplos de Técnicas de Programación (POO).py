# Definicion de Clase Padre
class Secretaria_Command_Center:
    def __init__(self, nombre, ultimatix):
        # Definir atributos de la clase Padre
        self.nombre = nombre
        self.ultimatix = ultimatix

    # Método para mostrar información básica
    def mostrar_informacion_basica(self):
        print("-------INFORMACION TRABAJADOR-------")
        print(f"Nombre: {self.nombre}")
        print(f"Ultimatix: {self.ultimatix}")


# Clases Heredadas
# Defino una clase Secretaria Tipo Documentación
class Secretaria_Documentacion(Secretaria_Command_Center):
    def __init__(self, nombre, ultimatix, rol):
        super().__init__(nombre, ultimatix)  # Llamo al constructor de la clase padre Secretaria_Command_Center
        self.rol = rol  # Atributo propio de la clase Secretaria_Documentacion

    # Método para mostrar información detallada
    def mostrar_informacion_detallada(self):
        super().mostrar_informacion_basica()  # Llamo al método heredado de la clase padre
        print(f"Rol: {self.rol}")


# Defino una clase Secretaria Tipo Coordinación
class Secretaria_Coordinacion(Secretaria_Command_Center):
    def __init__(self, nombre, ultimatix, rol):
        super().__init__(nombre, ultimatix)  # Llamo al constructor de la clase padre Secretaria_Command_Center
        self.rol = rol  # Atributo propio de la clase Secretaria_Coordinacion

    # Método para mostrar información detallada
    def mostrar_informacion_detallada(self):  # polimorfismo
        super().mostrar_informacion_basica()  # Llamo al método heredado de la clase padre
        print(f"Rol: {self.rol}")


# Defino una clase Secretaria Tipo Recepción
class Secretaria_Recepcion(Secretaria_Command_Center):
    def __init__(self, nombre, ultimatix, rol):
        super().__init__(nombre, ultimatix)  # Llamo al constructor de la clase padre Secretaria_Command_Center
        self.rol = rol  # Atributo propio de la clase Secretaria_Recepcion

    # Método para mostrar información detallada
    def mostrar_informacion_detallada(self):  # polimorfismo
        super().mostrar_informacion_basica()  # Llamo al método heredado de la clase padre
        print(f"Rol: {self.rol}")


# Defino una Clase Actividad para calcular el sueldo
class Actividad:
    def __init__(self, rol, sueldo=0):
        self.rol = rol
        self.__sueldo = sueldo  # Atributo privado

    def Rol_Documentacion(self):
        nombre_rol = "Documentación"
        print(f"---------------ROL: {nombre_rol}--------------")
        print("Actividades: Gestión y archivo de documentos")

    def Rol_Coordinacion(self):
        nombre_rol = "Coordinación"
        print(f"---------------ROL: {nombre_rol}--------------")
        print("Actividades: Coordinación de reuniones y eventos")

    def Rol_Recepcion(self):
        nombre_rol = "Recepción"
        print(f"---------------ROL: {nombre_rol}--------------")
        print("Actividades: Atención y orientación a visitantes")

    def sueldo_segun_actividad(self):  # polimorfismo con carga
        if self.rol == "Documentación":
            self.__sueldo = 850  # encapsulamiento
            self.Rol_Documentacion()
            print(f"Sueldo = {self.__sueldo}")
        elif self.rol == "Coordinación":
            self.Rol_Coordinacion()
            self.__sueldo = 1050  # encapsulamiento
            print(f"Sueldo = {self.__sueldo}")
        elif self.rol == "Recepción":
            self.Rol_Recepcion()
            self.__sueldo = 950  # encapsulamiento
            print(f"Sueldo = {self.__sueldo}")
        else:
            self.__sueldo = 500  # Sueldo base
        return self.__sueldo


# Ejemplo de uso

# Crear objeto ejemplo de la clase Documentación
secretaria_documentacion = Secretaria_Documentacion("Estefania", "831726", "Documentación")
secretaria_documentacion.mostrar_informacion_detallada()

# Crear objeto ejemplo de la clase Coordinación
secretaria_coordinacion = Secretaria_Coordinacion("Estefania", "731524", "Coordinación")
secretaria_coordinacion.mostrar_informacion_detallada()

# Crear objeto ejemplo de la clase Recepción
secretaria_recepcion = Secretaria_Recepcion("Estefania", "100229", "Recepción")
secretaria_recepcion.mostrar_informacion_detallada()

print("===========ACTIVIDADES Y SUELDOS============")
# Ejemplo de uso objetos para la actividad Documentación
actividad_documentacion = Actividad("Documentación")
actividad_documentacion.sueldo_segun_actividad()

# Ejemplo de uso objetos para la actividad Coordinación
actividad_coordinacion = Actividad("Coordinación")
actividad_coordinacion.sueldo_segun_actividad()

# Ejemplo de uso objetos para la actividad Recepción
actividad_recepcion = Actividad("Recepción")
actividad_recepcion.sueldo_segun_actividad()
