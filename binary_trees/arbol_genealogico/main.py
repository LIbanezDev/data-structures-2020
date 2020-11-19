import time


class Persona:
    def __init__(self, nombre: str, izq=None, der=None):
        self.nombre = nombre
        self.izq = izq
        self.der = der


def leer_arbol_from(nodo_actual: Persona or None):
    if nodo_actual is not None:
        print(nodo_actual.nombre)
        leer_arbol_from(nodo_actual.izq)
        leer_arbol_from(nodo_actual.der)


def recorrer_arbol_y_buscar(nodo_actual: Persona or None, nombre: str, persona_encontrada: Persona = None) -> Persona:
    if nodo_actual is not None and persona_encontrada is None:
        if nodo_actual.nombre == nombre:
            persona_encontrada = nodo_actual
        persona_encontrada = recorrer_arbol_y_buscar(nodo_actual.izq, nombre, persona_encontrada)
        persona_encontrada = recorrer_arbol_y_buscar(nodo_actual.der, nombre, persona_encontrada)
    return persona_encontrada


def crear_arbol_genealogico() -> Persona:  # 1
    return Persona("Juan",
                   Persona("Pedro", Persona("Antonio"), Persona("Claudia", Persona("Rosa", Persona("Mario")))),
                   Persona("Diego", Persona("Ester"), Persona("Marta")))


def buscar_persona(_raiz: Persona):  # 2
    nombre_a_buscar = input("Persona a buscar: ")
    persona_encontrada = recorrer_arbol_y_buscar(_raiz, nombre_a_buscar)
    if persona_encontrada is None:
        print("Persona no encontrada")
    else:
        print("Persona encontrada")


def listar_hijos(_raiz: Persona):  # 3
    nombre_a_listar = input("Nombre de persona para listar sus hijos: ")
    persona_encontrada = recorrer_arbol_y_buscar(_raiz, nombre_a_listar)
    if persona_encontrada is None:
        print("Persona no existe")
    else:
        has_hijo_derecho = persona_encontrada.der is not None
        has_hijo_izquerdo = persona_encontrada.izq is not None
        if not has_hijo_derecho and not has_hijo_izquerdo:
            print("No tiene hijos")
        if has_hijo_izquerdo:
            print(persona_encontrada.izq.nombre)
        if has_hijo_derecho:
            print(persona_encontrada.der.nombre)


def listar_descendencia(_raiz: Persona):  # 4
    nombre_a_listar = input("Nombre de persona para listar su descendencia: ")
    persona_encontrada = recorrer_arbol_y_buscar(_raiz, nombre_a_listar)
    if persona_encontrada is None:
        print("Persona no existe")
    else:
        has_hijo_derecho = persona_encontrada.der is not None
        has_hijo_izquerdo = persona_encontrada.izq is not None
        if not has_hijo_derecho and not has_hijo_izquerdo:
            print("No tiene descendencia")
        if has_hijo_izquerdo:
            leer_arbol_from(persona_encontrada.izq)
        if has_hijo_derecho:
            leer_arbol_from(persona_encontrada.der)


def determinar_paternidad(_raiz: Persona): # 5
    nombre_padre = input("Padre: ")
    nombre_hijo = input("Hijo: ")
    padre = recorrer_arbol_y_buscar(_raiz, nombre_padre)
    if padre is None:
        print("Padre no existe")
    else:
        es_padre = False
        if padre.der is not None:
            if padre.der.nombre == nombre_hijo:
                es_padre = True
        if padre.izq is not None:
            if padre.izq.nombre == nombre_hijo:
                es_padre = True
        if not es_padre:
            print(nombre_padre + " no es padre de " + nombre_hijo)
        else:
            print(nombre_padre + " si es padre de " + nombre_hijo)


print("Creando arbol...")
raiz = crear_arbol_genealogico()
time.sleep(.500)
print("Busque a una persona:")
buscar_persona(raiz)
listar_hijos(raiz)
listar_descendencia(raiz)
determinar_paternidad(raiz)
