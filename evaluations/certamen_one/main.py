# Lucas Ignacio Vergara Ibañez 192-B

class PALABRITA:
    palabra = ""
    cantidad = 0
    traduccion = None
    sinonimo = None
    siguiente = None


class WORDCITA:
    word = ""
    next = None


def AgregarPalabrasRecolectadas(baseEsp, baseIng):
    # Clonar variables recibidas en parametros para evitar duplicar el nombre desde otro scope
    nuevaBaseEsp, nuevaBaseIng = baseEsp, baseIng

    continuar = True
    while continuar:
        palabra = input("Ingrese palabra a agregar: ")
        idioma = input("Ingrese idioma de palabra ('E' / 'I'): ")
        if idioma == "E":
            objeto_palabra_esp = PALABRITA()
            objeto_palabra_esp.palabra = palabra
            if nuevaBaseEsp is None:  # Si base es nula, entonces base es la nueva palabra.
                objeto_palabra_esp.cantidad = 1
                nuevaBaseEsp = objeto_palabra_esp
            else:  # De lo contrario, agrega palabra al final
                iterator_esp = nuevaBaseEsp
                palabra_duplicada = False

                # Bucar palabra en lista de palabras en espanol.
                while iterator_esp.siguiente is not None and not palabra_duplicada:
                    if iterator_esp.palabra == palabra:
                        iterator_esp.cantidad += 1
                        palabra_duplicada = True
                    iterator_esp = iterator_esp.siguiente

                if not palabra_duplicada:
                    # Ya que el ultimo nodo no alcanzo a compararse en el while, entonces
                    # verifica si este es igual a la palabra ingresada
                    if iterator_esp.palabra == palabra:
                        iterator_esp.cantidad += 1
                    else:  # Si no es asi, agrega palabra en espanol al final.
                        objeto_palabra_esp.cantidad = 1
                        iterator_esp.siguiente = objeto_palabra_esp
        else:
            objeto_palabra_ing = WORDCITA()
            objeto_palabra_ing.word = palabra
            if nuevaBaseIng is None:  # Si base es nula, entonces base es la nueva palabra.
                nuevaBaseIng = objeto_palabra_ing
            else:  # De lo contrario, agrega palabra al final
                iterator_ing = nuevaBaseIng
                while iterator_ing.next is not None:
                    iterator_ing = iterator_ing.next
                iterator_ing.next = objeto_palabra_ing

        # Pregunta si desea continuar para terminar el bucle.
        desea_continuar = input("¿Desea continuar? ( si / no ): ")
        if desea_continuar == "no":
            continuar = False

    return nuevaBaseEsp, nuevaBaseIng


def ConectarSegunTraduccion(baseEsp, baseIng):
    palabra_esp = input("Ingrese palabra en espanhol: ")
    palabra_ing = input("Ingrese palabra en ingles: ")

    # Punteros que almacenaran la dir. en memoria de las palabras solicitadas
    palabra_esp_dir, palabra_ing_dir = None, None

    iterator_esp, iterator_ing = baseEsp, baseIng

    # Buscando la palabra en espanol en la lista de palabras en espanol.
    encontro_palabra_esp = False
    while iterator_esp is not None and not encontro_palabra_esp:
        if iterator_esp.palabra == palabra_esp:
            palabra_esp_dir = iterator_esp
            encontro_palabra_esp = True
        iterator_esp = iterator_esp.siguiente

    # Buscando la palabra en ingles en la lista de palabras en ingles.
    encontro_palabra_ing = False
    while iterator_ing is not None and not encontro_palabra_ing:
        if iterator_ing.word == palabra_ing:
            palabra_ing_dir = iterator_ing
            encontro_palabra_ing = True
        iterator_ing = iterator_ing.next

    # Si no encontro alguna, emite mensaje.
    if palabra_esp_dir is None or palabra_ing_dir is None:
        print("No se encontraron una de las dos palabras...")
        print(palabra_esp_dir, palabra_ing_dir)
    else:  # De lo contrario, conecta nodo "traduccion" con palabra en ingles
        palabra_esp_dir.traduccion = palabra_ing_dir


def ConectarSinonimos(baseEsp, baseIng):
    palabra_esp_one = input("Ingrese primer sinonimo: ")
    palabra_esp_two = input("Ingrese segunda sinonimo: ")

    palabra_esp_one_dir, palabra_esp_two_dir = None, None  # Almacenaran los punteros hacia palabras encontradas
    iterator_esp = baseEsp

    encontro_ambas = False
    while iterator_esp is not None and not encontro_ambas:

        # Verificador de si existe la palabra uno en la lista de palabras en espanol.
        if iterator_esp.palabra == palabra_esp_one:
            palabra_esp_one_dir = iterator_esp
            if palabra_esp_two_dir is not None:  # Si ya existe la otra (palabra_dos), entonces encontro ambas.
                encontro_ambas = True

        # Lo mismo con palabra dos.
        if iterator_esp.palabra == palabra_esp_two:
            palabra_esp_two_dir = iterator_esp
            if palabra_esp_one_dir is not None:
                encontro_ambas = True

        iterator_esp = iterator_esp.siguiente

    # Si encontro ambas, las conecta a traves del nodo "sinonimo" de cada una de ellas
    if palabra_esp_one_dir is not None and palabra_esp_two_dir is not None:
        palabra_esp_one_dir.sinonimo = palabra_esp_two_dir
        palabra_esp_two_dir.sinonimo = palabra_esp_one_dir
    else:  # No era necesario pero no costaba nada :)
        print("No se encontraron alguna de las 2 palabras")


def ConsultarPalabra(baseEsp, baseIng):
    palabra_buscada = input("Ingrese palabra a buscar: ")
    iterator_esp = baseEsp

    # Diccionario que almacena la direccion de memoria de la palabra y el idioma
    palabra_buscada_dir = {"direccion": None, "idioma": ""}

    # Verificador de si ha encontrado la palabra.
    encontro_palabra = False

    # Busca palabra en lista de palabras en espanhol.
    while iterator_esp is not None and not encontro_palabra:
        if iterator_esp.palabra == palabra_buscada:
            palabra_buscada_dir["direccion"] = iterator_esp
            palabra_buscada_dir["idioma"] = "Espanol"  # Evitando caracteres especiales (ñ)
            encontro_palabra = True
        iterator_esp = iterator_esp.siguiente

    # Si no la encontró, busca palabra en lista de palabras en ingles.
    if not encontro_palabra:
        iterator_ing = baseIng
        while iterator_ing is not None and not encontro_palabra:
            if iterator_ing.word == palabra_buscada:
                palabra_buscada_dir["direccion"] = iterator_ing
                palabra_buscada_dir["idioma"] = "Ingles"  # Evitando caracteres especiales (')
                encontro_palabra = True

    # Si no encuentra palabra en ninguna de las 2 listas, entonces no existe.
    if not encontro_palabra:
        print("Palabra no registrada aún!")
    else:
        # Obteniendo palabra e idioma de diccionario para manejo mas simple.
        palabra, idioma = palabra_buscada_dir["direccion"], palabra_buscada_dir["idioma"]

        # Si el idioma es espanol, se accede al atributo "palabra" del objeto
        # y se consulta por su sinonimo y traduccion.
        if idioma == "Espanol":
            print("Palabra buscada: " + palabra.palabra + " Idioma: " + idioma)
            if palabra.sinonimo is None:
                print("SIN SINONIMO.")
            else:
                print("Sinonimo de " + palabra.palabra + ": " + palabra.sinonimo.palabra)
            if palabra.traduccion is None:
                print("SIN TRADUCCION")
            else:
                print("Traduccion de " + palabra.palabra + ": " + palabra.traduccion.word)
        else:  # Si el idioma es ingles, se accede al atributo "word" del objeto
            print("Palabra buscada: " + palabra.word + " - Idioma: " + idioma)


def main():
    # PROGRAMA PRINCIPAL
    baseEsp, baseIng = None, None
    baseEsp, baseIng = AgregarPalabrasRecolectadas(baseEsp, baseIng)
    Opcion = "0"
    while Opcion != "9":
        print("Opciones: ")
        print("2: Conectar según traducción")
        print("3: Conectar sinónimos")
        print("4: Consultar palabra")
        print("9: Salir")
        Opcion = input("Ingrese opción: ")
        print()
        if Opcion == "2":
            ConectarSegunTraduccion(baseEsp, baseIng)
        if Opcion == "3":
            ConectarSinonimos(baseEsp, baseIng)
        if Opcion == "4":
            ConsultarPalabra(baseEsp, baseIng)
        if Opcion == "9":
            print("Fin de proceso")
        print()
    print()
    input()
