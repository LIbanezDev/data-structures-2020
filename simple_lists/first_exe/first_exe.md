2)	Se tiene una estructura de datos, que en realidad corresponde a varias listas .
La estructura principal es una lista simple de personas (ordenada por Rol),
conectadas mediante un puntero llamado next (conecta a todas las personas de la lista).
Pero también existen varias listas circulares separadas que son conectadas mediante el puntero hermano.
Class nodo():
    rol  =  0
    nombre  =  “    “
    sexo  =  “*”
    edad  =  0
    hermano  = None
    next = None
Se debe construir un programa COMPLETO en Python, que permita las siguientes opciones (presentar un menú y programar las
opciones usando procedimientos):
-	Agregar una nueva persona. Datos a ingresar: Rol, Nombre, Sexo,Edad.
    Inicialmente se supone que la nueva persona no tienen hermanos (el puntero hermano queda apuntando al mismo registro).
    Validar que ese Rol no existe previamente.
-	Conectar una persona a una lista de hermanos (esto es para personas que han sido recién
    ingresadas y se les quiere conectar con su(s) hermano(s)). Datos: Rol de la persona, Rol de uno de sus hermanos.
-	Listado de personas ordenadas por Rol. En el listado se debe indicar cuántos hermanos tiene cada persona.
-	Consultar por Rol. Se debe obtener los datos de la persona y los nombres de todos sus hermanos (si los tiene).
-	Eliminar una persona, por Rol. Importante: No se debe perder la integridad de las listas de hermanos existentes.
