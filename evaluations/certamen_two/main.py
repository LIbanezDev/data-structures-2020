import random

palabras = ["platano", "banana", "desarrollo", "crecimiento", "caro", "costoso", "barato", "economico", "gordo", "corpulento"]


class SUSTANTIVO:
    def __init__(self, palabra="", veces=0, siguiente=None):
        self.palabra = palabra
        self.veces = veces
        self.siguiente = siguiente


class NODO:
    def __init__(self, palabrita="", cantidad=0, sinonimo=None, izq=None, der=None):
        self.palabrita = palabrita
        self.cantidad = cantidad
        self.sinonimo = sinonimo  # Apunta a un sinónimo (si tiene) o es None.
        self.izq = izq
        self.der = der


def agregar_al_final(base: SUSTANTIVO, palabra: str) -> SUSTANTIVO:
    iterador = base
    encontro_palabra = False
    nueva_palabra = SUSTANTIVO(palabra, 1)
    if base is None:
        return nueva_palabra
    while iterador.siguiente is not None and not encontro_palabra:
        if iterador.palabra == palabra:
            iterador.veces += 1
            encontro_palabra = True
        iterador = iterador.siguiente
    if not encontro_palabra:
        if iterador.palabra == palabra:
            iterador.veces += 1
        else:
            iterador.siguiente = nueva_palabra
    return base


def LeerDatosYCrearLista(_BasePal):
    nueva_base = agregar_al_final(_BasePal, palabras[random.randint(0, len(palabras) - 1)])
    while random.randint(0, 10) != 9:
        nueva_base = agregar_al_final(nueva_base, palabras[random.randint(0, len(palabras) - 1)])
    return nueva_base


def leer_arbol(nodo_actual: NODO):
    global total, total_repetidas
    if nodo_actual is not None:
        total += nodo_actual.cantidad
        if nodo_actual.cantidad > 1:
            total_repetidas += 1
            print(nodo_actual.palabrita, nodo_actual.cantidad)
            if nodo_actual.sinonimo is not None:
                print("Sinonimo: " + nodo_actual.sinonimo.palabrita + "\n")
            else:
                print("Sinonimo: ****** \n")
        leer_arbol(nodo_actual.izq)
        leer_arbol(nodo_actual.der)


def CrearArbol(_BasePal, _RaizPal):
    iterador_lista = _BasePal
    nueva_raiz = None
    while iterador_lista is not None:
        if nueva_raiz is None:
            nueva_raiz = NODO(iterador_lista.palabra, iterador_lista.veces)
        else:
            iterador_arbol = nueva_raiz
            se_agrego = False
            while not se_agrego:
                if iterador_lista.palabra > iterador_arbol.palabrita:
                    if iterador_arbol.der is None:
                        iterador_arbol.der = NODO(iterador_lista.palabra, iterador_lista.veces)
                        se_agrego = True
                    else:
                        iterador_arbol = iterador_arbol.der
                else:
                    if iterador_arbol.izq is None:
                        iterador_arbol.izq = NODO(iterador_lista.palabra, iterador_lista.veces)
                        se_agrego = True
                    else:
                        iterador_arbol = iterador_arbol.izq
        iterador_lista = iterador_lista.siguiente
    return nueva_raiz


def conectar_sinonimos_pre_orden(nodo_actual: NODO, palabra_uno: str, palabra_dos: str):
    global sinonimo_uno, sinonimo_dos
    if nodo_actual is not None and (sinonimo_uno is None or sinonimo_dos is None):
        if nodo_actual.palabrita == palabra_uno:
            sinonimo_uno = nodo_actual
        elif nodo_actual.palabrita == palabra_dos:
            sinonimo_dos = nodo_actual
        conectar_sinonimos_pre_orden(nodo_actual.izq, palabra_uno, palabra_dos)
        conectar_sinonimos_pre_orden(nodo_actual.der, palabra_uno, palabra_dos)


def ConectarSinonimos(_RaizPal):
    palabra_uno = input("Sinonimo 1: ")
    palabra_dos = input("Sinonimo 2: ")
    conectar_sinonimos_pre_orden(_RaizPal, palabra_uno, palabra_dos)
    sinonimo_uno.sinonimo = sinonimo_dos
    sinonimo_dos.sinonimo = sinonimo_uno
    pass


def Listar(_RaizPal):
    global total, total_repetidas
    print("Nombre --- Cantidad de veces")
    leer_arbol(_RaizPal)
    print(total, total_repetidas)
    pass


# PROGRAMA PRINCIPAL
BasePal = None
RaizPal = None
BasePal = LeerDatosYCrearLista(BasePal)
RaizPal = CrearArbol(BasePal, RaizPal)
sinonimo_uno = None
sinonimo_dos = None
total = 0
total_repetidas = 0
Listar(RaizPal)
ConectarSinonimos(RaizPal)
Listar(RaizPal)
