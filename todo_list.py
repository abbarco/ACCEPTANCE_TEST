class Tarea:
    def __init__(self, nombre, completada=False):
        self.nombre = nombre
        self.completada = completada

class ListaTareas:
    def __init__(self):
        self.tareas = []
        self._output=""

    def agregar_tarea(self, nombre):
        nombre_lower = nombre.lower()
        for tarea in self.tareas:
            if tarea.nombre.lower() == nombre_lower:
                print(f"La tarea '{nombre}' ya existe en la lista.")
                self._output = f"La tarea '{nombre}' ya existe en la lista."
                return
        tarea = Tarea(nombre)
        self.tareas.append(tarea)
        print(f"Tarea '{nombre}' agregada a la lista.")
        self._output = f"Tarea '{nombre}' agregada a la lista."

    def listar_tareas(self):
        if not self.tareas:
            print("\nNo hay tareas por mostrar.")
            self._output = "No hay tareas por mostrar."
        else:
            salida="\nLista de tareas:\n" + "\n".join([f"{i + 1}. {tarea.nombre} - {'Completada' if tarea.completada else 'Pendiente'}" for i, tarea in enumerate(self.tareas)])
            self._output = salida
            print(salida)
            
    def marcar_completada(self, numero_tarea):
        if 1 <= numero_tarea <= len(self.tareas):
            tarea = self.tareas[numero_tarea - 1]
            tarea.completada = True
            self._output = f"\nTarea '{tarea.nombre}' marcada como completada."
            print(f"\nTarea '{tarea.nombre}' marcada como completada.")
        else:
            print("\nNúmero de tarea inválido.")
            self._output = "\nNúmero de tarea inválido."

    def borrar_tareas(self):
        self.tareas = []
        print("\nLista de tareas borrada.")

    def output(self):
        return self._output

def main():
    lista_tareas = ListaTareas()

    while True:
        print("\nMenu:")
        print("1. Agregar tarea")
        print("2. Listar tareas")
        print("3. Marcar tarea como completada")
        print("4. Borrar lista de tareas")
        print("5. Salir")

        opcion = input("\nIngrese el número de la opción: ")

        if opcion == "1":
            nombre_tarea = input("\nIngrese el nombre de la tarea: ")
            lista_tareas.agregar_tarea(nombre_tarea)
        elif opcion == "2":
            lista_tareas.listar_tareas()
        elif opcion == "3":
            if not lista_tareas.tareas:
                print("Primero debe ingresar una tarea.")
            else:
                numero_tarea = int(input("\nIngrese el número de la tarea a marcar como completada: "))
                lista_tareas.marcar_completada(numero_tarea)
        elif opcion == "4":
            lista_tareas.borrar_tareas()
        elif opcion == "5":
            print("\n¡Hasta luego!")
            break
        else:
            print("\nOpción inválida. Ingrese una opción válida.")

if __name__ == "__main__":
    main()
