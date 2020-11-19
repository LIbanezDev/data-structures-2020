import datetime
import random

from faker import Faker

faker = Faker()

tipo_transaccion = ["A", "G"]


class Cliente:
    def __init__(self, num_cuenta: int, nombre: str = "", ahorro: int = 0, izq=None, der=None):
        self.num_cuenta = num_cuenta
        self.nombre = nombre
        self.ahorro = ahorro
        self.izq = izq
        self.der = der


class Transaccion:
    def __init__(self, tipo: str, monto: int, cuenta: Cliente, siguiente=None):
        self.cuenta = cuenta
        self.tipo = tipo
        self.monto = monto
        self.fecha = datetime.datetime.now()
        self.siguiente = siguiente


def agregar_transaccion(_base: Transaccion or None) -> Transaccion:
    nueva_base = _base
    if nueva_base is None:
        nueva_base = Transaccion(
            tipo_transaccion[random.randint(0, 1)],
            random.randint(1000, 10000),
            Cliente(random.randint(100, 115), faker.name())
        )
    iterador = nueva_base
    for i in range(random.randint(8, 10)):
        iterador.siguiente = Transaccion(
            tipo_transaccion[random.randint(0, 1)],
            random.randint(1000, 10000),
            Cliente(random.randint(100, 115), faker.name())
        )
        iterador = iterador.siguiente
    return nueva_base


def agregar_al_arbol(_raiz: Cliente, _transaccion: Transaccion) -> Cliente or None:
    if _raiz is None:
        return _transaccion.cuenta
    else:
        iterador_arbol = _raiz
        agrego_cliente = False
        while not agrego_cliente:
            if _transaccion.cuenta.num_cuenta == iterador_arbol.num_cuenta:
                if _transaccion.tipo == "A":
                    iterador_arbol.ahorro += _transaccion.monto
                else:
                    iterador_arbol.ahorro -= _transaccion.monto
                agrego_cliente = True
            else:
                nuevo_cliente = _transaccion.cuenta
                if _transaccion.tipo == "A":
                    nuevo_cliente.ahorro += _transaccion.monto
                else:
                    nuevo_cliente.ahorro -= _transaccion.monto
                if _transaccion.cuenta.num_cuenta > iterador_arbol.num_cuenta:
                    if iterador_arbol.der is None:
                        iterador_arbol.der = nuevo_cliente
                        agrego_cliente = True
                    else:
                        iterador_arbol = iterador_arbol.der
                else:
                    if iterador_arbol.izq is None:
                        iterador_arbol.izq = nuevo_cliente
                        agrego_cliente = True
                    else:
                        iterador_arbol = iterador_arbol.izq
        return _raiz


def crear_y_actualizar_arbol(_base: Transaccion or None) -> Cliente or None:
    if _base is None:
        return None
    iterador_transacciones = _base
    nueva_raiz = None
    while iterador_transacciones is not None:
        nueva_raiz = agregar_al_arbol(nueva_raiz, iterador_transacciones)
        iterador_transacciones = iterador_transacciones.siguiente
    return nueva_raiz


def recorrer_arbol(_raiz: Cliente or None):
    global monto_total
    if _raiz is None:
        print("No hay clientes para listar!!!!")
        return
    print("Listado ordenado por numero de cuenta: ")
    recorrido_en_orden(_raiz)
    print("Monto total acumulado:", str(monto_total))


def recorrido_en_orden(cliente_actual: Cliente or None):
    global monto_total
    if cliente_actual is not None:
        monto_total += cliente_actual.ahorro
        recorrido_en_orden(cliente_actual.izq)
        if cliente_actual.ahorro > 1500:
            print("Numero de cuenta:", str(cliente_actual.num_cuenta) + "\nNombre:", cliente_actual.nombre + "\nAhorro total:",
                  str(cliente_actual.ahorro) + "\n")
        recorrido_en_orden(cliente_actual.der)


monto_total = 0


def main():
    base_transacciones = None
    base_transacciones = agregar_transaccion(base_transacciones)
    raiz_clientes = crear_y_actualizar_arbol(base_transacciones)
    recorrer_arbol(raiz_clientes)
