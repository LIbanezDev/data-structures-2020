import random
from faker import Faker

faker = Faker()

tipos_contacto = ["C", "E", "T"]


class Contacto:
    def __init__(self, tipo: str, contacto: str, siguiente=None):
        self.tipo = tipo
        self.contacto = contacto
        self.siguiente = siguiente


class Empleado:
    def __init__(self, codigo: int, nombre: str, ape_paterno: str, ape_materno: str, siguiente_codigo=None,
                 siguiente_paterno=None, primer_contacto=None):
        self.codigo = codigo
        self.nombre = nombre
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.siguiente_codigo = siguiente_codigo
        self.siguiente_paterno = siguiente_paterno
        self.primer_contacto = primer_contacto
