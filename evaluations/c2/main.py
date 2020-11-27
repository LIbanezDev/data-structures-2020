# Lucas Vergara Ibañez 192 - B

# Mi idea es desarrollar un modulo por cada punto solicitado (4), pero tambien utilizar modulos helpers o de ayuda para
# reutilizar el codigo a traves de estos 4 modulos.

# El rut pudo interpretarse como string o integer, elegi integer para que la comparacion entre un rut mayor o menor
# sea mas clara, por lo tanto hay que evitar el -
class Esposo:
    def __init__(self, rut: int, nombre: str, sexo: str, conyuge=None, prim_hijo=None, izq=None, der=None):
        self.rut = rut
        self.nombre = nombre
        self.sexo = sexo  # Se usará “M” o “F”
        self.conyuge = conyuge  # Apunta al nodo de la esposa o del esposo.
        self.prim_hijo = prim_hijo  # Es None o apunta a un nodo del árbol de hijos.
        self.izq = izq
        self.der = der


class Hijo:
    def __init__(self, rut: int, nombre: str, sexo: str, primogenito: str, izq=None, der=None):
        self.rut = rut
        self.nombre = nombre
        self.sexo = sexo  # Se usará “M” o “F”
        self.primogenito = primogenito  # Se usará “S” o “N”
        self.izq = izq
        self.der = der


# Modulos generales de busqueda y recorrido de arboles (1)
# Este modulo tiene el objetivo de buscar un nodo realizando un recorrido exaustivo de tipo "pre-orden" utilizando la clave rut
# como parametro de busqueda
def buscar_nodo_arbol(nodo_actual, rut: int, nodo_buscado=None):
    if nodo_actual is not None and nodo_buscado is None:
        if rut == nodo_actual.rut:
            nodo_buscado = nodo_actual
        nodo_buscado = buscar_nodo_arbol(nodo_actual.izq, rut, nodo_buscado)
        nodo_buscado = buscar_nodo_arbol(nodo_actual.der, rut, nodo_buscado)
    return nodo_buscado


# Modulos generales de busqueda y recorrido de arboles (2)
# Esta funcion tiene el objetivo de agregar nodo al final de cualquier arbol ordenado por el atributo "rut"
def agregar_nodo_arbol(_raiz: Esposo or Hijo, nuevo_nodo: Esposo or Hijo) -> Esposo or Hijo:
    iterador_raiz = _raiz
    ultimo = None
    while iterador_raiz is not None:
        ultimo = iterador_raiz
        if nuevo_nodo.rut > iterador_raiz.rut:
            iterador_raiz = iterador_raiz.der
        else:
            iterador_raiz = iterador_raiz.izq
    if _raiz is None:  # Si base es nula, agrega el nuevo nodo
        _raiz = nuevo_nodo
    else:  # De lo contrario, agrega el nuevo nodo en el puntero derecha o izquerda dependiendo del rut
        if nuevo_nodo.rut > ultimo.rut:
            ultimo.der = nuevo_nodo
        else:
            ultimo.izq = nuevo_nodo
    return _raiz


# Punto 1
def agregar_matrimonio(_raiz: Esposo or None) -> Esposo:
    # Solicitar datos de esposos
    rut_esposo = int(input("Rut esposo: "))
    rut_esposa = int(input("Rut esposa: "))
    nombre_esposo = input("Nombre esposo: ")
    nombre_esposa = input("Nombre esposa: ")
    esposo = Esposo(rut_esposo, nombre_esposo, "M")
    esposa = Esposo(rut_esposa, nombre_esposa, "F")

    # Conectar nodo conyuge
    esposo.conyuge = esposa
    esposa.conyuge = esposo

    # Clonar raiz recibida en parametros para mas orden
    nueva_raiz = _raiz

    # Si base es nula, crea el arbol de 0 con los nuevos matrimonios
    if nueva_raiz is None:
        if rut_esposo < rut_esposa:
            esposo.der = esposa
            nueva_raiz = esposo
        else:
            esposa.der = esposo
            nueva_raiz = esposa
        return nueva_raiz

    # Si base no es nula, entonces se agrega ambos esposos al arbol correspondiente
    nueva_raiz = agregar_nodo_arbol(nueva_raiz, esposo)
    nueva_raiz = agregar_nodo_arbol(nueva_raiz, esposa)

    return nueva_raiz


# Punto 2
def agregar_hijo(_raiz_hijos: Hijo or None, _raiz_esposos: Esposo) -> Hijo or None:
    nueva_raiz_hijos = _raiz_hijos
    rut_padre = int(input("Rut de uno de los padres: "))

    # Validar que padre existe
    padre = buscar_nodo_arbol(raiz_esposos, rut_padre)
    if padre is None:
        print("El padre ingresado no existe")
        return nueva_raiz_hijos

    # Validar que hijo ya existe previamente
    rut_hijo = int(input("Rut de hijo: "))
    hijo_existente = buscar_nodo_arbol(_raiz_hijos, rut_hijo)
    if hijo_existente is not None:  # Si existe, cancelar operacion
        print("Hijo ya existe")
        return nueva_raiz_hijos

    # Solicitar datos restantes
    es_primogenito = input("Es primogenito? (s/n)").upper()
    nombre_hijo = input("Nombre de hijo: ")
    sexo_hijo = input("Sexo (m/f): ").upper()
    nuevo_hijo = Hijo(rut_hijo, nombre_hijo, sexo_hijo, es_primogenito)

    # Aregar nuevo nodo al arbol de hijos con la ayuda de una funcion helper
    nueva_raiz_hijos = agregar_nodo_arbol(nueva_raiz_hijos, nuevo_hijo)

    if es_primogenito == "S":  # Si es primogenito, el nodo "prim_hijo" de sus padres queda apuntando al nuevo hijo
        padre.prim_hijo = nuevo_hijo
        padre.conyuge.prim_hijo = nuevo_hijo

    return nueva_raiz_hijos


# Funcion de ayuda para punto 2 y 3
# Sirve para buscar los padres de un hijo en el arbol de esposos.
def buscar_padre_de_hijo(nodo_actual, rut_hijo, esposo=None) -> Esposo:
    if nodo_actual is not None and esposo is None:
        if nodo_actual.prim_hijo is not None:
            if nodo_actual.prim_hijo.rut == rut_hijo:
                esposo = nodo_actual
        esposo = buscar_padre_de_hijo(nodo_actual.izq, rut_hijo, esposo)
        esposo = buscar_padre_de_hijo(nodo_actual.der, rut_hijo, esposo)
    return esposo


# Punto 3
def listar_en_orden_hijos(nodo_actual: Hijo, _raiz_esposos):
    if nodo_actual is not None:
        listar_en_orden_hijos(nodo_actual.izq, raiz_esposos)
        if nodo_actual.primogenito == "S":
            padre_uno = buscar_padre_de_hijo(raiz_esposos, nodo_actual.rut)
            padre_dos = padre_uno.conyuge
            if padre_uno.sexo == "M":
                nombre_padre = padre_uno.nombre
                nombre_madre = padre_dos.nombre
            else:
                nombre_padre = padre_dos.nombre
                nombre_madre = padre_uno.nombre
            print("Rut: ", nodo_actual.rut, "Nombre: ", nodo_actual.nombre, "Nombre padre: ", nombre_padre, "Nombre madre: ", nombre_madre)
        listar_en_orden_hijos(nodo_actual.der, raiz_esposos)


# Funciones de ayuda para parte 4 (1)
# Retorna el total de personas casadas, el cual luego se divide en 2 para obtener los matrimonios totales.
# Retorna el total de personas sin hijos, el cual tambien se divide en 2 para obtener el total de matrimonios sin hijos
def calcular_matrimonios(nodo_actual: Esposo, total=0, total_sin_hijos=0) -> [int, int]:
    if nodo_actual is not None:
        total += 1
        if nodo_actual.prim_hijo is None:
            total_sin_hijos += 1
        total, total_sin_hijos = calcular_matrimonios(nodo_actual.izq, total, total_sin_hijos)
        total, total_sin_hijos = calcular_matrimonios(nodo_actual.der, total, total_sin_hijos)
    return total, total_sin_hijos


# Funciones de ayuda para parte 4 (2)
# Retorna el total de hijos y de hijos primogenitos.
def calcular_hijos(nodo_actual: Hijo, total=0, total_primogenitos=0) -> [int, int]:
    if nodo_actual is not None:
        total += 1
        if nodo_actual.primogenito == "S":
            total_primogenitos += 1
        total, total_primogenitos = calcular_hijos(nodo_actual.izq, total, total_primogenitos)
        total, total_primogenitos = calcular_hijos(nodo_actual.der, total, total_primogenitos)
    return total, total_primogenitos


# Punto 4
def desplegar_estadisticas(_raiz_hijos: Hijo, _raiz_matrimonios: Esposo):
    matr_totales, matr_sin_hijos = calcular_matrimonios(_raiz_matrimonios)
    hijos_totales, hijos_primogenitos = calcular_hijos(_raiz_hijos)
    print("Matrimonios totales: " + str(int(matr_totales / 2)))  # Aplicando int() para eliminar decimales
    print("Matrimonios totales sin hijos: " + str(int(matr_sin_hijos / 2)))
    print("Total de hijos: " + str(hijos_totales))
    print("Total de hijos primogenitos: " + str(hijos_primogenitos))


raiz_esposos = None
raiz_hijos = None
continuar = True
while continuar:
    print("1. Agregar Matrimonio")
    print("2. Agregar nuevo hijo")
    print("3. Lista de hijos ordenado por RUT de hijos primogenitos")
    print("4. Desplegar estadisticas")
    opc = input("Opcion: ")
    if opc == "1":
        raiz_esposos = agregar_matrimonio(raiz_esposos)
    elif opc == "2":
        raiz_hijos = agregar_hijo(raiz_hijos, raiz_esposos)
    elif opc == "3":
        listar_en_orden_hijos(raiz_hijos, raiz_esposos)
    elif opc == "4":
        desplegar_estadisticas(raiz_hijos, raiz_esposos)
    else:
        print("Opcion no reconocida")
    c = input("Desea continuar?")
    if c == "n":
        continuar = False
