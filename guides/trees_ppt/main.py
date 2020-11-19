import faker
import random

faker = faker.Faker()


class PersonaL:
    def __init__(self, nombre: str, edad: int, siguiente=None):
        self.nombre = nombre
        self.edad = edad
        self.siguiente = siguiente


class PersonaT:
    def __init__(self, nombre: str, edad: int, izq=None, der=None):
        self.nombre = nombre
        self.edad = edad
        self.izq = izq
        self.der = der


def pre_orden(_raiz: PersonaT or None):
    if _raiz is not None:
        print(_raiz.edad, _raiz.nombre)
        pre_orden(_raiz.izq)
        pre_orden(_raiz.der)


def buscar_persona_pre_orden(nodo_actual: PersonaT, name: str, persona_buscada=None) -> PersonaT or None:
    if nodo_actual is not None and persona_buscada is None:
        if nodo_actual.nombre == name:
            persona_buscada = nodo_actual
        persona_buscada = buscar_persona_pre_orden(nodo_actual.izq, name, persona_buscada)
        persona_buscada = buscar_persona_pre_orden(nodo_actual.der, name, persona_buscada)
    return persona_buscada


def buscar_persona_arbol(_raiz: PersonaT or None):
    nombre = input("Nombre de persona a buscar: ")
    persona_buscada = buscar_persona_pre_orden(_raiz, nombre)
    if persona_buscada is None:
        print("Persona no existe")
    else:
        print(persona_buscada.nombre, persona_buscada.edad)


def agregar_nodo_arbol_busqueda(_raiz: PersonaT or None, name: str, age: int) -> PersonaT:
    nueva_persona = PersonaT(name, age)
    if _raiz is None:
        return nueva_persona
    iter_arbol = _raiz
    ultimo = None
    while iter_arbol is not None:
        ultimo = iter_arbol
        if age >= iter_arbol.edad:
            iter_arbol = iter_arbol.der
        else:
            iter_arbol = iter_arbol.izq
    if age >= ultimo.edad:
        ultimo.der = nueva_persona
    else:
        ultimo.izq = nueva_persona
    return _raiz


def crear_arbol(_raiz: PersonaT or None) -> PersonaT:
    for i in range(random.randint(25, 40)):
        name = faker.name()
        age = random.randint(10, 50)
        _raiz = agregar_nodo_arbol_busqueda(_raiz, name, age)
    return _raiz


def agregar_nodo_lista_ordenada(_base: PersonaL, name: str, age: int) -> PersonaL:
    nueva_persona = PersonaL(name, age)
    if _base is None or age <= _base.edad:
        nueva_persona.siguiente = _base
        _base = nueva_persona
    else:
        iterador = _base
        anterior = None
        while iterador is not None and iterador.edad < nueva_persona.edad:
            anterior = iterador
            iterador = iterador.siguiente
        nueva_persona.siguiente = iterador
        anterior.siguiente = nueva_persona
    return _base


def crear_lista(_base_personas: PersonaL or None) -> PersonaL:
    nueva_base = _base_personas
    continuar = True
    while continuar:
        nueva_base = agregar_nodo_lista_ordenada(nueva_base, faker.name(), random.randint(10, 30))
        resp = input("Desea continuar? s/n")
        if resp == "n":
            continuar = False
    return nueva_base


raiz_personas = None
# base_personas = None
# base_personas = crear_lista(base_personas)
raiz_personas = crear_arbol(raiz_personas)
pre_orden(raiz_personas)
buscar_persona_arbol(raiz_personas)
