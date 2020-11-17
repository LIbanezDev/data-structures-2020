def PreOrden(Puntero):
    if Puntero is not None:
        print(Puntero.Valor)
        PreOrden(Puntero.Izq)
        PreOrden(Puntero.Der)


def InOrden(Puntero):
    if Puntero is not None:
        InOrden(Puntero.Izq)
        print(Puntero.Valor)
        InOrden(Puntero.Der)


def PostOrden(Puntero):
    if Puntero is not None:
        PostOrden(Puntero.Izq)
        PostOrden(Puntero.Der)
        print(Puntero.Valor)
