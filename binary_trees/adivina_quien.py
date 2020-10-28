"""
Mini adivina quien utilizando la estructura de datos arbol binario
"""


class Nodo:
    pregunta: ""
    si: None
    no: None

    def __init__(self, pregunta="", si=None, no=None):
        self.pregunta = pregunta
        self.si = si
        self.no = no


def main():
    raiz = Nodo("Es un hombre", Nodo("Pedro"), Nodo("Maria"))
    continuar = True
    while continuar:
        iterador = raiz
        while iterador.si is not None:
            respuesta = input("¿" + iterador.pregunta + "? (s / n): ").lower()
            if respuesta == "s":
                iterador = iterador.si
            elif respuesta == "n":
                iterador = iterador.no
            else:
                print("La respuesta debe ser (s / n)")

        respuesta = input("¿La persona en la que estaba pensando es " + iterador.pregunta + "? - (s / n): ").lower()
        if respuesta == "s":
            print("He ganado!")
        elif respuesta == "n":
            nombre = input("He perdido... ¿Como se llamaba la persona en la que estaba pensando?: ").lower()
            pregunta_input = input("¿Que pregunta diferencia a " + nombre + " de " + iterador.pregunta + "?: ").lower()
            respuesta = input("¿Cual es la respuesta a aquella pregunta? - (s / n): ")
            print("Gracias, ahora conozco a otra persona")
            if respuesta == "s":
                iterador.si = Nodo(nombre)
                iterador.no = Nodo(iterador.pregunta)
            else:
                iterador.no = Nodo(nombre)
                iterador.si = Nodo(iterador.pregunta)
            iterador.pregunta = pregunta_input
        else:
            print("??")

        desea_continuar = input("¿Desea continuar? - (s / n)").lower()
        if desea_continuar == "n":
            continuar = False
