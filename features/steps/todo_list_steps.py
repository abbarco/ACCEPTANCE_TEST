from behave import *
from todo_list import *

#Administración de tareas
@given('que la lista de tareas está vacía')
def step_impl(context):
    context.lista_tareas = ListaTareas()

@when('agrego una tarea con nombre "{nombre}"')
def step_impl(context, nombre):
    context.lista_tareas.agregar_tarea(nombre)

@then('veo un mensaje que dice "{mensaje}"')
def step_impl(context, mensaje):
    assert mensaje in context.lista_tareas.output(), f"El mensaje '{mensaje}' no está en la salida"

#Marcar una tarea como completada
@given('que la lista de tareas contiene tareas')
def step_impl(context):
    context.lista_tareas = ListaTareas()
    for row in context.table:
        tarea = Tarea(row['Tarea'], completada=row['Estado'] == 'Completada')
        context.lista_tareas.tareas.append(tarea)

@when('el usuario marca la tarea "{nombre_tarea}" como completada')
def step_impl(context, nombre_tarea):
    for tarea in context.lista_tareas.tareas:
        if tarea.nombre == nombre_tarea:
            tarea.completada = True
            break

@then('la lista de tareas debería mostrar la tarea "{nombre_tarea}" como completada')
def step_impl(context, nombre_tarea):
    tarea_encontrada = False
    for tarea in context.lista_tareas.tareas:
        if tarea.nombre == nombre_tarea:
            assert tarea.completada, f"La tarea '{nombre_tarea}' no está marcada como completada"
            tarea_encontrada = True
            break
    assert tarea_encontrada, f"No se encontró la tarea '{nombre_tarea}' en la lista"

#Borrar toda la lista de tareas
@given('que tengo una lista de tareas con tareas existentes')
def step_given_tareas_existentes(context):
    context.lista_tareas = ListaTareas()
    context.lista_tareas.agregar_tarea("Buy groceries")
    context.lista_tareas.agregar_tarea("Pay bills")

@when('borro la lista de tareas')
def step_when_borrar_lista_tareas(context):
    context.lista_tareas.borrar_tareas()

@then('la lista de tareas debería estar vacía')
def step_then_lista_vacia(context):
    assert not context.lista_tareas.tareas

#Listar todas las tareas en la lista
@when('listo las tareas')
def step_when_listar_tareas(context):
    context.lista_tareas.listar_tareas()

@then('veo la lista de tareas')
def step_then_ver_lista_tareas(context):
    expected_output = "Lista de tareas:\n1. Buy groceries - Pendiente\n2. Pay bills - Pendiente"
    actual_output = context.lista_tareas.output().strip()  # Eliminar espacios en blanco al principio y al final
    assert actual_output == expected_output

#Intentar cambiar el estado de una tarea en lista vacía
@when('intento cambiar el estado de una tarea')
def step_when_intentar_cambiar_estado(context):
    context.lista_tareas.marcar_completada(1)  # Intentamos cambiar el estado de una tarea (que no existe)

@then('debería ver un mensaje de error indicando que la lista está vacía')
def step_then_ver_mensaje_error_lista_vacia(context):
    expected_output = "\nNúmero de tarea inválido."
    actual_output = context.lista_tareas.output()
    assert actual_output == expected_output