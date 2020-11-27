<h1> Ejercicio tipo certamen 2 - Arboles Binarios </h1>

En el gobierno que administra cierta isla se desea almacenar los datos de sus habitantes en una estructura de datos conformada por dos árboles binarios de búsqueda (ordenados por Rol, clave = Rol). Uno de los árboles (apuntado por RaizMasc) contendrá datos de los hombres de la isla y el otro árbol (apuntado por RaizFem) contendrá datos de las mujeres de la isla. Ver figura que muestra como podría quedar la estructura al final del proceso (para ciertos datos de prueba). Existe un puntero (conyuge) en que en caso de matrimonio el nodo del hombre apuntará al nodo de su esposa y el nodo de la mujer apuntará al nodo de su esposo. 

Se debe utilizar la siguiente definición de nodo para los dos árboles. No se acepta que se modifique la estructura de registros: 

```python  
class  HABITANTE:
    def __init__(self):
        self.rol = 0
        self.nombre = ""  
        self.edad = 0  
        self.conyuge = None # Apunta al cónyuge, si tiene (o es None).  
        self.izq = None 
        self.der = None 

# Observación: Son dos árboles (con el mismo tipo de nodo), cada uno apuntado por su raíz   (RaizMasc   y   RaizFem). Al principio ambas raíces deben comenzar con el valor None.  Note que no está el dato de sexo (esa condición está incorporada en el árbol en que está cada nodo). 
# Por otra parte, se utilizará una lista simple para almacenar inicialmente los datos de las personas de la isla (Rol, Nombre, Sexo, Edad), pero la información de matrimonios existentes se ingresará posteriormente. El registro que corresponde al nodo de esta lista es el siguiente: 

class  PERSONA:
    def __init__(self):
        self.rol = 0
        self.nombre = ""  
        self.edad = 0  
        self.sexo = "" # Se usa “M” para Masculino y “F” para Femenino.   
        self.siguiente = None 
```
Esta lista estará apuntada por el puntero BasePer que debe comenzar en None. 
                 
Se pide un programa Python completo que realice siguientes procesos en forma consecutiva:
1.	Crear y agregar nodos a la lista de datos de personas (se van agregando al final de la lista o en cualquier otra parte, pero se debe revisar que el Rol no está ya incluido en esa lista; si ya lo estuviera, no se debe crear un nuevo nodo). Se supone que la lista comienza vacía. Este proceso debe permitir ir ingresando los datos de todos los habitantes, por teclado. Manejar de alguna manera la cantidad de personas que deben ingresarse. Validaciones: Que no exista ya ese Rol en la lista, si ya existiera no se agrega a la lista ese nodo de nuevo.  
2.	Crear los dos árboles (de hombres y de mujeres) en base a la lista de datos de personas. Cada nodo de esa lista debe generar un nodo en uno de los dos árboles (en el que corresponda según el sexo). 
3.	Proceso “Matrimonear”. Se debe conectar los nodos de los dos árboles que correspondan a un matrimonio. Para ello, para cada matrimonio existente se debe ingresar el Rol del hombre y en segundo lugar el Rol de la mujer. Ambos existirán en su correspondiente árbol, ya que se supone que no existe error de datos. El algoritmo debe conectar ambos nodos. Manejar de alguna manera la cantidad de matrimonios que deben ingresarse. 




4.	Obtener listado de todos los habitantes, recorriendo los dos árboles (NO LA LISTA DE DATOS DE PERSONAS). En el listado se debe indicando los datos de cada habitante (Rol, Nombre, Edad, Sexo, Cónyuge). En el caso de Cónyuge debe anotarse el nombre del esposo(a) o la palabra “SOLTERO”. Al final del listado se debe indicar: Cantidad total de habitantes, Cantidad de matrimonios, Cantidad de hombres solteros, Cantidad de mujeres solteras.
