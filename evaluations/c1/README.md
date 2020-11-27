<h1> Certamen 1  EDD - Semestre 2 - 2020 </h1>

Un estudiante está empezando un estudio que tiene que ver con palabras del lenguaje español y del lenguaje inglés.

Para ello, va recolectando palabras de ambos idiomas y necesita un programa que las vaya almacenando en dos listas simples. La que contendrá palabras en español quedará apuntada por el puntero BaseEsp y la que contendrá palabras en inglés quedará apuntada por el puntero BaseIng.

Ambas listas tendrán nodos que corresponden a registros diferentes.

El registro que corresponde a palabra en español tendrá los siguientes campos: palabra, cantidad, traduccion, sinonimo y siguiente. El campo palabra contendrá la palabra (string). El campo cantidad servirá para obtener la cantidad de veces que ha sido encontrada esa palabra. Los otros 3 campos son punteros. El puntero traduccion será None o apuntará a una palabra de la otra lista (lista de palabras en inglés). El puntero sinonimo será None o apuntará a otra palabra de la misma lista. El puntero siguiente permitirá conectar con la siguiente palabra.

Se debe utilizar la siguiente definición de nodo para la lista de palabras en español e ingles:

```python
class PALABRITA:
    palabra = ""
    cantidad = 0
    traduccion = None
    sinonimo = None
    siguiente = None

class WORDCITA:
    word = ""
    next = None
```

Se pide un programa Python completo que realice siguientes procesos los que serán activados por un programa Principal que además contendrá un menú (ver más abajo el Programa Principal):

1.	Agregar palabras recolectadas a las listas. Debe ser un proceso repetitivo (usted debe controlar cómo terminar la iteración (NO USAR BREAK). En cada iteración, el usuario debe ingresar como datos: una palabra (string) y el carácter “E” (español) o “I” (inglés). Cada palabra debe agregarse al final de la lista correspondiente, según sea el idioma. Se supone que la listas comienzan vacías. Este proceso debe permitir ingresar los datos de un socio por teclado. Los datos a ingresar son: Palabra, Idioma (“E” o “I”). En el caso de que la palabra esté en español y ya existiera en la lista, no se agrega un nuevo nodo, sino que se aumenta en 1 la cantidad de ocurrencias de esa palabra. Si es nueva palabra en español, se agrega al final de la lista y el campo cantidad queda con el valor 1.

2.	Conectar según traducción. Datos a ingresar (en este orden): Palabra en español, Palabra en inglés. Validar que exista cada palabra en la lista correspondiente. Si no existiera alguna, no se realiza la operación de conexión. Si no hay error, el puntero traduccion de la palabra en español debe quedar apuntando a la palabra en inglés (no se apunta nada desde inglés a español). .

3.	Conectar sinónimos. Se ingresan dos palabras en español que ya existen. Una vez que se ubiquen, cada puntero sinonimo debe apuntar a la otra palabra (quedan apuntadas mutuamente. No es necesario validar nada.

4.	Consultar por alguna palabra. Dato a ingresar: Palabra (puede ser palabra en español o en inglés). Si la palabra no existe, se debe indicar eso. Si existe, se debe informar: Palabra, Idioma (“Español” o “Inglés”), Palabra de traducción (si existe conexión con una palabra del otro idioma, o “SIN TRADUCCIÓN”) y Palabra sinónimo (si tiene sinónimo o “SIN SINÖNIMO”).
