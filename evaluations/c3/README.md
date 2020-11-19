<h2> Certamen dos S2 - 2020 </h2>

Suponer que en cierta organización hay personas que mantienen dinero como ahorro. Los datos de ahorro se mantienen en un árbol binario ordenado de búsqueda (clave de ordenamiento = NumCuenta), apuntado por RaizCuentas (ver figura ejemplo). 
Cada nodo de este árbol tiene los siguientes campos: NumCuenta, NombreSocio, MontoAhorro, puntero izquierdo, puntero derecho. 
Por otra parte, en una estructura de lista simple se tienen los datos de transacciones que se han hecho sobre esas cuentas de ahorro durante cierto periodo de tiempo. La lista está apuntada por BaseTran
Cada nodo de la lista tiene los siguientes datos: Fecha, CuentaTran, TipoTran, MontoTran puntero siguiente. 
Fecha es la fecha de la transacción (ejemplo “17/12/2019”). 
CuentaTran es la cuenta a la que se aplica la transacción. 
TipoTran puede ser “A” para abono (se aumenta el ahorro de la cuenta) o “G” para giro (se disminuye el ahorro de la cuenta). 
MontoTran es la cantidad de dinero que se está abonando o girando. 
Puntero siguiente es el puntero que enlaza con el siguiente nodo. 
  

Se pide un programa Python que realice tres procesos en forma consecutiva:
1.	Crear y agregar nodos a la lista de transacciones que se han hecho sobre las cuentas de ahorro durante cierto periodo de tiempo (se van agregando al final de la lista). Se supone que la lista comienza vacía. Este proceso debe permitir ir ingresando las transacciones por teclado. Manejar de alguna manera la cantidad de transacciones que deben ingresarse.
2.	Crear y actualizar el árbol de cuentas, en base a las transacciones. Se supone que el árbol comienza vacío. A medida que se procesan las transacciones se van agregando nuevos nodos o se van actualizando los nodos ya existentes. Para cada transacción procesada puede pasar lo siguiente: 
3.	Si no existe en el árbol un nodo con ese número de cuenta, se agrega un nuevo nodo al árbol y se suma o se resta el monto de la transacción al MontoAhorro (que comienza en cero). 
4.	Si ya existe un nodo con ese número de cuenta en el árbol, se suma o se resta el MontoTran a MontoAhorro. 
5.	Listar los datos de las cuentas con MontoAhorro mayor que 30000 (recorrer el árbol con método En-Orden para obtener listado ordenado por NumCuenta). Al final del listado indicar el monto total ahorrado (suma de todos los MontoAhorro). 


```python
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
    pass

def crear_y_actualizar_arbol(_base: Transaccion or None) -> Cliente or None: 
    pass
 
def recorrido_en_orden(cliente_actual: Cliente or None):
    pass

```
