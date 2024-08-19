import threading
import time

# Definir las tareas
def tarea_1():
    for i in range(5):
        print(f"Tarea 1 - Iteración {i + 1}")
        time.sleep(1)  # Simular una tarea que toma tiempo

def tarea_2():
    for i in range(5):
        print(f"Tarea 2 - Iteración {i + 1}")
        time.sleep(1.5)  # Simular una tarea que toma tiempo

def tarea_3():
    for i in range(5):
        print(f"Tarea 3 - Iteración {i + 1}")
        time.sleep(2)  # Simular una tarea que toma tiempo

# Crear los hilos
hilo_1 = threading.Thread(target=tarea_1)
hilo_2 = threading.Thread(target=tarea_2)
hilo_3 = threading.Thread(target=tarea_3)

# Iniciar los hilos
hilo_1.start()
hilo_2.start()
hilo_3.start()

# Esperar a que los hilos terminen
hilo_1.join()
hilo_2.join()
hilo_3.join()

print("Todas las tareas han finalizado.")
