
import os
import datetime

# Función para agregar una nueva tarea
def agregar_tarea():
    titulo = input("Ingrese el título de la tarea: ")
    descripcion = input("Ingrese la descripción de la tarea: ")
    fecha_vencimiento = input("Ingrese la fecha de vencimiento (AAAA-MM-DD): ")
    
    with open("tareas_pendientes.txt", "a") as file:
        file.write(f"{titulo}\n{descripcion}\n{fecha_vencimiento}\n")

# Función para listar todas las tareas pendientes
def listar_tareas():
    with open("tareas_pendientes.txt", "r") as file:
        lines = file.readlines()
        for i in range(0, len(lines), 3):
            titulo = lines[i].strip()
            descripcion = lines[i+1].strip()
            fecha_vencimiento = lines[i+2].strip()
            print(f"Título: {titulo}")
            print(f"Descripción: {descripcion}")
            print(f"Fecha de vencimiento: {fecha_vencimiento}")
            print("=" * 30)

# Función para marcar una tarea como completada
def marcar_completada():
    listar_tareas()
    tarea_completada = input("Ingrese el número de la tarea que desea marcar como completada: ")
    
    with open("tareas_pendientes.txt", "r") as file:
        lines = file.readlines()
    
    with open("tareas_pendientes.txt", "w") as file:
        for i in range(0, len(lines), 3):
            if i != (int(tarea_completada) - 1) * 3:
                file.write(lines[i])
                file.write(lines[i+1])
                file.write(lines[i+2])
    
    # Mover la tarea completada a la lista de tareas completadas
    with open("tareas_completadas.txt", "a") as file:
        file.write(lines[(int(tarea_completada) - 1) * 3])
        file.write(lines[(int(tarea_completada) - 1) * 3 + 1])
        file.write(lines[(int(tarea_completada) - 1) * 3 + 2])

# Función para mostrar tareas vencidas o próximas a vencerse
def mostrar_tareas_vencidas():
    with open("tareas_pendientes.txt", "r") as file:
        lines = file.readlines()
        today = datetime.date.today()
        for i in range(0, len(lines), 3):
            fecha_vencimiento = datetime.date.fromisoformat(lines[i + 2].strip())
            if fecha_vencimiento < today:
                titulo = lines[i].strip()
                descripcion = lines[i + 1].strip()
                print(f"Título: {titulo}")
                print(f"Descripción: {descripcion}")
                print(f"Fecha de vencimiento: {fecha_vencimiento}")
                print("=" * 30)

# Función principal
def main():
    while True:
        print("\n--- Lista de Tareas ---")
        print("1. Agregar una tarea")
        print("2. Listar tareas pendientes")
        print("3. Marcar tarea como completada")
        print("4. Mostrar tareas vencidas")
        print("5. Salir")
        
        opcion = input("Seleccione una opción: ")
        
        if opcion == "1":
            agregar_tarea()
        elif opcion == "2":
            listar_tareas()
        elif opcion == "3":
            marcar_completada()
        elif opcion == "4":
            mostrar_tareas_vencidas()
        elif opcion == "5":
            break
        else:
            print("Opción no válida. Intente de nuevo.")

if __name__ == "__main__":
    if not os.path.exists("tareas_pendientes.txt"):
        open("tareas_pendientes.txt", "w").close()
    if not os.path.exists("tareas_completadas.txt"):
        open("tareas_completadas.txt", "w").close()
    
    main()
