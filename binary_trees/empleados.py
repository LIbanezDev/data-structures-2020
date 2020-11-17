class Empleado:
    def __init__(self, cod_empleado: int, nombre: str, edad: int, sexo: str, izq=None, der=None):
        self.cod_empleado = cod_empleado
        self.nombre = nombre
        self.edad = edad
        self.sexo = sexo
        self.izq = izq
        self.der = der


def agregar_empleado(_raiz: Empleado) -> Empleado:
    codigo = int(input("Codigo de empleado a agregar: "))
    iterator = _raiz
    ultimo_nodo = None
    while iterator is not None and iterator.cod_empleado != codigo:
        ultimo_nodo = iterator
        if codigo > iterator.cod_empleado:
            iterator = iterator.der
        else:
            iterator = iterator.izq
    if iterator is not None:
        print("Codigo de empleado ya existe...")
        return _raiz
    nombre = input("Nombre: ")
    edad = int(input("Edad: "))
    sexo = input("Sexo: ")
    nuevo_nodo = Empleado(codigo, nombre, edad, sexo)
    if _raiz is None:
        return nuevo_nodo
    elif codigo > ultimo_nodo.cod_empleado:
        ultimo_nodo.der = nuevo_nodo
    else:
        ultimo_nodo.izq = nuevo_nodo
    return _raiz


def listar(_raiz: Empleado):
    sexo = 'M'
    edad = 5
    if _raiz is not None:
        if _raiz.sexo == sexo and _raiz.edad >= edad:
            print("Nombre: %s, edad: %s, sexo: %s  " % (_raiz.nombre, _raiz.edad, _raiz.sexo))
        listar(_raiz.izq)
        listar(_raiz.der)


raiz = None
opcion = -1
while opcion != 3:
    opcion = int(input("Ingrese opcion"))
    if opcion == 1:
        raiz = agregar_empleado(raiz)
    if opcion == 2:
        listar(raiz)
