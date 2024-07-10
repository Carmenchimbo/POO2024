# Este programa calcula el área de diferentes figuras geométricas.
# Se utilizan diferentes tipos de datos (integer, float, string, boolean) y convenciones de nomenclatura.

def calcular_area_circulo(radio):
    """
    Calcula el área de un círculo dado su radio.
    :param radio: Radio del círculo (float)
    :return: Área del círculo (float)
    """
    pi = 3.14159  # Valor aproximado de π
    area = pi * radio ** 2
    return area

def calcular_area_rectangulo(ancho, alto):
    """
    Calcula el área de un rectángulo dado su ancho y alto.
    :param ancho: Ancho del rectángulo (float)
    :param alto: Alto del rectángulo (float)
    :return: Área del rectángulo (float)
    """
    area = ancho * alto
    return area

def calcular_area_triangulo(base, altura):
    """
    Calcula el área de un triángulo dado su base y altura.
    :param base: Base del triángulo (float)
    :param altura: Altura del triángulo (float)
    :return: Área del triángulo (float)
    """
    area = (base * altura) / 2
    return area

def main():
    # Variables para almacenar los resultados
    area_circulo = calcular_area_circulo(5.0)  # Radio del círculo
    area_rectangulo = calcular_area_rectangulo(4.0, 6.0)  # Ancho y alto del rectángulo
    area_triangulo = calcular_area_triangulo(3.0, 7.0)  # Base y altura del triángulo

    # Mostrar los resultados
    print("Área del círculo con radio 5.0:", area_circulo)
    print("Área del rectángulo con ancho 4.0 y alto 6.0:", area_rectangulo)
    print("Área del triángulo con base 3.0 y altura 7.0:", area_triangulo)

    # Ejemplo de uso de booleano
    es_mayor_area_circulo = area_circulo > area_rectangulo
    print("¿El área del círculo es mayor que el área del rectángulo?", es_mayor_area_circulo)

if __name__ == "__main__":
    main()