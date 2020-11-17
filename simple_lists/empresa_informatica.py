from faker import Faker
import random

fake = Faker()


class Contacto:
    def __init__(self, tipo: str, contacto: str, siguiente: None = None):
        self.tipo = tipo
        self.contacto = contacto
        self.siguiente = siguiente


class Empleado:
    def __init__(self, cod_empleado: int, nombre: str, ape_paterno: str, ape_materno: str,
                 siguiente_codigo=None,
                 siguiente_paterno=None,
                 primer_contacto: Contacto or None = None):
        self.cod_empleado = cod_empleado
        self.nombre = nombre
        self.ape_paterno = ape_paterno
        self.ape_materno = ape_materno
        self.siguiente_codigo = siguiente_codigo
        self.siguiente_paterno = siguiente_paterno
        self.primer_contacto = primer_contacto


def get_existe_codigo(_base: Empleado, codigo: int) -> bool:
    iterador = _base
    encontro_codigo = False
    while iterador is not None and not encontro_codigo:
        if iterador.cod_empleado == codigo:
            encontro_codigo = True
        iterador = iterador.siguiente_codigo
    return encontro_codigo


def agregar_empleado(_base: Empleado) -> Empleado:
    codigo_empleado = random.randint(1, 150)
    existe_codigo = get_existe_codigo(_base, codigo_empleado)
    if existe_codigo:
        print("Empleado con el codigo", str(codigo_empleado), "ya existe")
        return _base
    nombre: str = fake.first_name()
    ape_paterno: str = fake.last_name()
    ape_materno: str = fake.last_name()
    contactos = None
    ingresar_empleados = True
    if ingresar_empleados:
        base_contactos = Contacto(random.choice(["C", "E", "T"]), fake.phone_number())
        ultimo_contacto = base_contactos
        for i in range(random.randint(3, 10)):
            nuevo_contacto = Contacto(random.choice(["C", "E", "T"]), fake.phone_number())
            ultimo_contacto.siguiente = nuevo_contacto
            ultimo_contacto = nuevo_contacto
        contactos = base_contactos
    if _base is None:
        return Empleado(codigo_empleado, nombre, ape_paterno, ape_materno, None, None, contactos)
    iterador_codigo, iterador_paterno = _base.siguiente_codigo, _base.siguiente_paterno
    se_agrego = False
    ultimo_codigo = None
    nuevo_empleado = Empleado(codigo_empleado, nombre, ape_paterno, ape_materno, None, None, contactos)
    while iterador_codigo is not None and not se_agrego:
        ultimo_codigo = iterador_codigo
        if iterador_codigo.cod_empleado < codigo_empleado:
            if iterador_codigo.siguiente_codigo is not None:
                nuevo_empleado.siguiente_codigo = iterador_codigo.siguiente_codigo.siguiente_codigo
            iterador_codigo.siguiente_codigo = nuevo_empleado
            se_agrego = True
        iterador_codigo = iterador_codigo.siguiente_codigo
    if not se_agrego:
        if ultimo_codigo is not None:
            ultimo_codigo.siguiente_codigo = nuevo_empleado
        else:
            _base.siguiente_codigo = nuevo_empleado
    return _base


base = None
for x in range(5):
    base = agregar_empleado(base)
