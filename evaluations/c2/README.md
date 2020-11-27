<h1> Certamen 2 - EDD - Semestre 2 - 2020 </h1>

En cierta sociedad, se decide tener los datos de los integrantes de las familias en dos estructuras tipo árbol: 
 
Árbol de esposos. Es un árbol binario ordenado de búsqueda (clave = RUT). Suponer que siempre las personas están con su cónyuge en el árbol, por lo que existe un puntero que los une. Además hay un puntero hacia el hijo primogénito (que está en el otro árbol) o None si no tienen hijos. El árbol está apuntado por RaizEsposos. La estructura de la clase registro es la siguiente: 
  
```python  
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
```

Se pide un programa completo que presente un menú que permita las siguientes operaciones  (15 puntos por cosas generales):
-	Agregar un nuevo matrimonio (son dos nodos). Datos: RUT esposo, RUT esposa, Nombre esposo, Nombre esposa. Se deben agregar ambos nodos al árbol y conectarse entre sí (en ambos sentidos). No se pide validar existencia previa (pero hay que preocuparse de caso inicial, es decir árbol vacío). (20 puntos) 
-	Agregar un nuevo hijo. Datos: RUT padre (o madre), RUT nuevo hijo, ¿Es primogénito? (“Sí” o “No”), Nombre hijo, Sexo hijo. El proceso debe agregar ese nuevo hijo al Árbol de hijos, como nodo terminal. Además si fuera primogénito, se debe poner el puntero hacia ese nodo en los nodos de ambos padres (campo PrimHijo). Se pide validar existencia previa de ese hijo (si ya existía, no se hace nada). Además hay que preocuparse del primer caso, es decir árbol vacío). (20 puntos) 
-	Listado de hijos ordenado por RUT de hijos primogénitos. Para cada hijo que cumpla ser primer hijo se debe escribir su RUT, Nombre, Nombre de padre, Nombre de madre. (35 puntos)
-	Estadísticas: Obtener cantidad de matrimonios, Cantidad de matrimonios sin hijos, Cantidad total de hijos existentes en el segundo árbol, Cantidad total de hijos primogénitos. (25 puntos) 

