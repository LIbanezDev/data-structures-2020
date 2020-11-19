<h2> Ejercicio Tipo Certamen </h2>

Cierto estudiante está estudiando la frecuencia en que aparecen palabras que son sustantivos en un texto. Para ello decide utilizar 2 estructuras de datos para almacenar las palabras y sus frecuencias. Una lista simple (datos: Palabra, Veces) y un árbol binario ordenado (clave = palabrita). Ver figura que muestra como podría quedar la estructura al final del proceso (para ciertos datos de prueba). Existe un puntero (sinonimo) en que en caso de que dos palabras sean sinónimos entre si, se apuntarán mutuamente. 

Se utilizará una lista simple para almacenar inicialmente los datos de palabras (Palabra, Veces que aparece), pero la información de sinónimos existentes se ingresará posteriormente. El registro que corresponde al nodo de esta lista es el siguiente (no se acepta que se modifique la estructura de registros): 

```python
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
```

Observación: La lista debe estar apuntada por BasePal y el árbol debe estar apuntado por RaizPal. Al principio tanto BasePal como RaizPal deben comenzar con el valor None. 


Se pide un programa Python completo que realice siguientes procesos en forma consecutiva (al principio del programa, en comentarios ponga su nombre completo y curso):

1.	Crear y agregar nodos a la lista de palabras. En el caso de palabras nuevas (que no están ya en la lista) se van agregando al final de la lista, con dato cantidad = 1. Si la palabra ya existe, simplemente se debe incrementar el contador (Veces). La lista comienza vacía. Este proceso debe permitir ir ingresando palabras por teclado (ver en la figura ejemplo de palabras ingresadas). Manejar de alguna manera la cantidad de palabras que deben ingresarse. 

2.	Crear el árbol en base a la lista de palabras. Cada nodo de la lista debe generar un nodo en el árbol. El árbol debe quedar ordenado por Palabra (árbol ordenado de búsqueda), en la figura usted puede ver que ese árbol fue generado desde la lista y quedó como árbol ordenado de búsqueda (clave = palabrita). Note que las palabras menores (alfabéticamente) quedan hacia el lado izquierdo y las mayores (alfabéticamente) quedan hacia el lado derecho. Les recuerdo que Python puede comparar directamente dos palabras para saber cuál es menor y cuál mayor (no es necesario comparar letra por letra). En el campo sinonimo al principio queda un None. 

3.	Proceso “Conectar sinónimos”. Se debe conectar los dos nodos del árbol que correspondan a sinónimos. Para ello, se deben ingresar las dos palabras que son sinónimos (ambos existirán en el árbol, ya que se supone que no existe error de datos). El algoritmo debe conectar ambos nodos. Manejar de alguna manera la cantidad de pares de sinónimos que deben ingresarse (en el ejemplo, se supone que se ingresaron los pares “PORCINO” – “CERDO” y “BANANA” – “PLATANO”. 

4.	Obtener listado de todos los palabras que han aparecido más de una vez, recorriendo el árbol (NO LA LISTA DE PALABRAS). En el listado se debe indicar los datos de cada palabra que está más de una vez (Palabra, Veces que está, Sinónimo). Si tiene sinónimo debe anotarse la palabra sinónimo o “*****” si no lo tiene. Al final del listado se debe indicar: Cantidad total de palabras y Cantidad de palabras que aparecen más de 1 vez. El listado debe aparecer ordenado por palabras (alfabético). En el ejemplo: BANANA – CERDO – LAPIZ – ZAPATO. 
