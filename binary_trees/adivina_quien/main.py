class Pregunta:
    def __init__(self, pregunta: str, si=None, no=None):
        self.pregunta = pregunta
        self.si = si
        self.no = no


def crear_arbol() -> Pregunta:
    return Pregunta("¿Vive en el agua?",
                    Pregunta("¿Tiene una especie llamada Koi?", Pregunta("Pez"), Pregunta("Rana")),
                    Pregunta("¿Es un felino?", Pregunta("Gatito"), Pregunta("Raton")))


def crear_archivo(actual_puntero: Pregunta, archivo, _pregunta: str, direccion: str):
    if actual_puntero is not None:
        archivo.write(actual_puntero.pregunta + ";" + _pregunta + ";" + direccion + "\n")
        crear_archivo(actual_puntero.si, archivo, actual_puntero.pregunta, "S")
        crear_archivo(actual_puntero.no, archivo, actual_puntero.pregunta, "N")


def leer_pre_orden(_raiz: Pregunta):
    if _raiz is not None:
        print(_raiz.pregunta)
        leer_pre_orden(_raiz.si)
        leer_pre_orden(_raiz.no)


def buscar_pregunta(punt: Pregunta, _pregunta: str):
    global punt_padre
    if punt is not None and punt_padre is None:
        if punt.pregunta == _pregunta:
            punt_padre = punt
        buscar_pregunta(punt.no, _pregunta)
        buscar_pregunta(punt.si, _pregunta)


def leer_archivo() -> Pregunta or None:
    archivo = open('adivina_quien.txt', 'r')
    _raiz = None
    for linea in archivo:
        linea_array = linea.strip().split(";")
        print(linea_array)
        _pregunta, padre, direccion = linea_array
        if padre == "*":
            _raiz = Pregunta(_pregunta)
        else:
            buscar_pregunta(_raiz, padre)
            nuevo_nodo = Pregunta(_pregunta)
            if direccion == "S":
                punt_padre.si = nuevo_nodo
            else:
                punt_padre.no = nuevo_nodo
    archivo.close()
    return _raiz


punt_padre = None


def main():
    raiz = leer_archivo()
    continuar = True
    while continuar:
        print("Piense en un animal y yo tratare de adivinarlo...")
        iterador = raiz
        while iterador.si is not None or iterador.no is not None:
            resp = input("El animal que ud penso " + iterador.pregunta).lower()
            if resp == "si":
                iterador = iterador.si
            else:
                iterador = iterador.no

        resp = input("¿El animal es " + iterador.pregunta + "?").lower()
        if resp == "si":
            print("He ganado")
        else:
            animal = input("He perdido, ¿En que animal estabas pensando?")
            pregunta = input("Cual pregunta diferencia a " + iterador.pregunta + " de " + animal)
            preg_full = pregunta + "?"
            resp_preg = input("Cual es la respuesta a " + preg_full + " para " + animal).lower()
            if resp_preg == "si":
                iterador.si = Pregunta(animal)
                iterador.no = Pregunta(iterador.pregunta)
            else:
                iterador.si = Pregunta(iterador.pregunta)
                iterador.no = Pregunta(animal)
            iterador.pregunta = preg_full
            archivo_a_escribir = open("adivina_quien.txt", "w")
            crear_archivo(raiz, archivo_a_escribir, "*", "*")
            archivo_a_escribir.close()
            print("Gracias, ahora conozco otro animal.")
main()