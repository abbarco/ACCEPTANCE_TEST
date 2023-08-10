Feature: Administración de tareas
    Scenario: Agregar tarea
        Given que la lista de tareas está vacía
        When agrego una tarea con nombre "Hacer compras"
        Then veo un mensaje que dice "Tarea 'Hacer compras' agregada a la lista"

    Scenario: Marcar una tarea como completada
        Given que la lista de tareas contiene tareas:
        | Tarea         | Estado   |
        | Comprar víveres | Pendiente |
        When el usuario marca la tarea "Comprar víveres" como completada
        Then la lista de tareas debería mostrar la tarea "Comprar víveres" como completada
    

    Scenario: Borrar toda la lista de tareas
        Given que tengo una lista de tareas con tareas existentes
        When borro la lista de tareas
        Then la lista de tareas debería estar vacía

    Scenario: Listar todas las tareas en la lista
        Given que tengo una lista de tareas con tareas existentes
        When listo las tareas
        Then veo la lista de tareas

#Escenario propio creado
    Scenario: Intentar cambiar el estado de una tarea en lista vacía
        Given que la lista de tareas está vacía
        When intento cambiar el estado de una tarea
        Then debería ver un mensaje de error indicando que la lista está vacía