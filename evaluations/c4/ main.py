# Lucas Vergara Ibañez 192 - B

import random

from faker import Faker

faker = Faker()

generos = ["M", "F"]


class Habitante:
    def __init__(self, rol: int, nombre: str, edad: int, conyuge=None, izq=None, der=None):
        self.rol = rol
        self.nombre = nombre
        self.edad = edad
        self.conyuge = conyuge  # Apunta al cónyuge, si tiene (o es None).
        self.izq = izq
        self.der = der


class Persona:
    def __init__(self, rol: int, sexo: str, nombre: str = "", edad: int = 0, siguiente=None):
        self.rol = rol
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.siguiente = siguiente


def LeerDatosYCrearLista(_base_personas: None) -> Persona:
    nueva_base = Persona(random.randint(1, 100), generos[random.randint(0, 1)], faker.name(), random.randint(18, 50))
    iteador_base = nueva_base
    continuar = True
    while continuar:
        rol: int = 0
        rol_correcto = False
        while not rol_correcto:
            rol = int(input("Ingrese rol: "))
            existe = False
            iter_busca_rol = nueva_base
            while iter_busca_rol is not None and not existe:
                if iter_busca_rol.rol == rol:
                    print("Rol ya ingresado, reintente...")
                    existe = True
                iter_busca_rol = iter_busca_rol.siguiente
            if not existe:
                rol_correcto = True
        iteador_base.siguiente = Persona(rol, generos[random.randint(0, 1)], faker.name(), random.randint(18, 50))
        iteador_base = iteador_base.siguiente
        continua = input("Desea continuar? s/n")
        if continua == "n":
            continuar = False
    return nueva_base


def agregar_al_final_arbol(_raiz: Habitante, persona: Persona) -> Habitante:
    nuevo_habitante = Habitante(persona.rol, persona.nombre, persona.edad)
    if _raiz is None:
        return nuevo_habitante
    iterador_arbol = _raiz
    agrego_habitante = False
    while not agrego_habitante:
        if nuevo_habitante.rol > iterador_arbol.rol:
            if iterador_arbol.der is None:
                iterador_arbol.der = nuevo_habitante
                agrego_habitante = True
            else:
                iterador_arbol = iterador_arbol.der
        else:
            if iterador_arbol.izq is None:
                iterador_arbol.izq = nuevo_habitante
                agrego_habitante = True
            else:
                iterador_arbol = iterador_arbol.izq
    return _raiz


def buscar_habitante_en_arbol(_raiz: Habitante, rol: int) -> Habitante:
    iterador = _raiz
    habitante_buscado = None
    while iterador is not None and habitante_buscado is None:
        if rol == iterador.rol:
            habitante_buscado = iterador
        if rol > iterador.rol:
            iterador = iterador.der
        else:
            iterador = iterador.izq
    return habitante_buscado


def leer_lista(_base: Persona or None):
    if _base is not None:
        print(_base.rol, _base.sexo)
        leer_lista(_base.siguiente)


def CrearArboles(_base_personas: Persona, raiz_masculina: None, raiz_femenina: None) -> [Habitante, Habitante]:
    iterador_personas = _base_personas
    while iterador_personas is not None:
        if iterador_personas.sexo == "M":
            raiz_masculina = agregar_al_final_arbol(raiz_masculina, iterador_personas)
        else:
            raiz_femenina = agregar_al_final_arbol(raiz_femenina, iterador_personas)
        iterador_personas = iterador_personas.siguiente
    return raiz_masculina, raiz_femenina


def Matrimonear(raiz_masculina: Habitante, raiz_femeina: Habitante):
    continuar = True
    while continuar:
        rol_hombre = int(input("Rol de hombre a matrimonear: "))
        rol_mujer = int(input("Rol de mujer a matrimonear: "))
        hombre_a_matrimonear = buscar_habitante_en_arbol(raiz_masculina, rol_hombre)
        mujer_a_matrimonear = buscar_habitante_en_arbol(raiz_femeina, rol_mujer)
        hombre_a_matrimonear.conyuge = mujer_a_matrimonear
        mujer_a_matrimonear.conyuge = hombre_a_matrimonear
        print("Matrimonio establecido.")
        resp = input("Desea continuar matrimoneando? s/n")
        if resp == "n":
            continuar = False


def recorrido_exaustivo_arbol(nodo_actual: Habitante, sexo: str, h=0, m=0, sm=0, sf=0) -> [int, int, int, int]:
    if nodo_actual is not None:
        print("Rol", str(nodo_actual.rol), "Nombre:", nodo_actual.nombre, "edad:", str(nodo_actual.edad), "sexo:", sexo)
        if nodo_actual.conyuge is not None:
            print("Conyuge:", nodo_actual.conyuge.nombre)
            m += 1
        else:
            if sexo == "M":
                sm += 1
            else:
                sf += 1
        h += 1
        h, m, sm, sf = recorrido_exaustivo_arbol(nodo_actual.izq, sexo, h, m, sm, sf)
        h, m, sm, sf = recorrido_exaustivo_arbol(nodo_actual.der, sexo, h, m, sm, sf)
    return [h, m, sm, sf]


def Listar(raiz_masculina: Habitante, raiz_femenina: Habitante):
    print("Listado de habitantes...")
    suma_habitantes, suma_matrimonios, suma_solteros, suma_solteras = recorrido_exaustivo_arbol(raiz_masculina, "M")
    suma_habitantes, suma_matrimonios, suma_solteros, suma_solteras = recorrido_exaustivo_arbol(raiz_femenina, "F",
                                                                                                suma_habitantes,
                                                                                                suma_matrimonios, suma_solteros,
                                                                                                suma_solteras)
    print("-- Estadisticas --")
    print("Habitantes: " + str(suma_habitantes))
    print("Matrimonios: " + str(suma_matrimonios))
    print("Hombres solteros: " + str(suma_solteros))
    print("Mujeres solteras: " + str(suma_solteras))
    pass


def main():
    BasePer = None
    RaizMasc = None
    RaizFem = None
    BasePer = LeerDatosYCrearLista(BasePer)
    RaizMasc, RaizFem = CrearArboles(BasePer, RaizMasc, RaizFem)
    leer_lista(BasePer)
    Matrimonear(RaizMasc, RaizFem)
    Listar(RaizMasc, RaizFem)
