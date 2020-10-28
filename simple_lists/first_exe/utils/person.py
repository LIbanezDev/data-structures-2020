import random


class Persona:
    id = 0
    rol = 0
    nombre = ""
    sexo = ""
    edad = 0
    email = ""
    next = None
    brother = None

    def __init__(self, _id, name, gender, age, email):
        self.nombre = name
        self.sexo = gender
        self.email = email
        self.edad = age
        self.id = _id

    def set_initial_hermano(self, myself):
        self.brother = myself

    def set_rol(self, rol):
        self.rol = rol


def agregar_persona(base, persona):
    genders = ['M', 'F']
    persona_entity = Persona(
        persona["id"],
        persona["name"],
        random.choice(genders),
        random.randint(8, 28),
        persona["email"]
    )
    persona_entity.set_initial_hermano(persona_entity)
    if base is None:
        base = persona_entity
    else:
        iterator = base
        random_rol = random.randint(1, 10)
        last = None
        roles = []
        while iterator is not None:
            roles.append(iterator.rol)
            if iterator.next is None:
                last = iterator
            iterator = iterator.next

        roles.append(last.rol)

        while random_rol in roles:
            random_rol = random.randint(1, 10)
        last.next = persona_entity
        last.next.set_rol(random_rol)
    return base


def eliminar_hermano(hermano):
    iterator = hermano.brother
    while iterator is not hermano:
        if iterator.brother is hermano:
            iterator.brother = iterator
        elif iterator.brother.brother is hermano:
            iterator.brother = iterator.brother.brother
            break
        iterator = iterator.brother


def eliminar_persona(base, rol):
    if base is None:
        print("No hay personas aun!")
        return None
    if base.rol == rol:
        if base.next is None:
            base = None
        else:
            if base.next.brother is base.next:
                base.next.brother = base.next
            base = base.next

        print("Persona de rol " + str(rol) + " se ha eliminado correctamente")
        return base
    iterator = base
    se_elimino = False
    while iterator is not None:
        if iterator.next.rol == rol:
            if iterator.next.next is not None:
                iterator.next = iterator.next.next
                eliminar_hermano(iterator.next)
            else:
                eliminar_hermano(iterator.next)
                iterator.next = None
            se_elimino = True
            break
        iterator = iterator.next
    if se_elimino:
        print("Persona de rol " + str(rol) + " se ha eliminado correctamente")
    else:
        print("Persona no encontrada")
    return base


def listar_persona(base, rol):
    iterator = base
    if base is None:
        print("No hay personas aun!")
        return None
    persona_buscada = None
    while iterator is not None:
        if iterator.rol == rol:
            persona_buscada = iterator
        iterator = iterator.next
    if persona_buscada is None:
        print("Persona no existe")
        return None

    persona_buscada_bros = persona_buscada.brother
    print(
        "Nombre " + persona_buscada.nombre + ", sexo: " + persona_buscada.sexo + ", edad: " + str(persona_buscada.edad))
    numero_hermano = 0
    if persona_buscada is not persona_buscada_bros:
        while persona_buscada_bros is not persona_buscada:
            numero_hermano += 1
            print("Nombre hermano " + str(numero_hermano) + ": " + persona_buscada_bros.nombre)
            persona_buscada_bros = persona_buscada_bros.brother
    if numero_hermano == 0:
        print("No tiene hermanos.")

    return True


def listar_personas(base):
    if base is None:
        print("No hay personas aun!")
        return False

    iterator = base

    print("\n---- Listado ----")
    while iterator is not None:
        iterator_brothers_base = iterator.brother
        print("ID:" + str(iterator.id) + " - Nombre:" + iterator.nombre + " - Sexo:" + iterator.sexo + " - Edad:" + str(
            iterator.edad) + " - Rol: " + str(iterator.rol))
        count = 1

        while iterator_brothers_base is not iterator:
            print("Hermano numero " + str(count) + ": " + iterator_brothers_base.nombre)
            iterator_brothers_base = iterator_brothers_base.brother
            count += 1
        iterator = iterator.next

    print("--------------------\n")


def ordenar_por_rol(base):
    ite_rol = base
    while ite_rol is not None:
        print(ite_rol.rol)
        ite_rol = ite_rol.next


def add_brother(base, sender_rol, receiver_rol):
    ite_bro = base
    sender = None
    receiver = None

    if base is None:
        print("No hay gente en la lista!!!!!!")
        return False

    while ite_bro is not None:
        if ite_bro.rol == sender_rol:
            sender = ite_bro
        if ite_bro.rol == receiver_rol:
            receiver = ite_bro
        if sender is not None and receiver is not None:
            break
        ite_bro = ite_bro.next

    if sender is None or receiver is None:
        print("Relacion no agregada, uno de los hermanos no existe.")
        return False

    if sender.brother is not sender:
        relacion_establecida = False
        ite_brothers = sender.brother
        while ite_brothers is not sender:
            if ite_brothers is receiver:
                relacion_establecida = False
                break
            if ite_brothers.brother is sender:
                ite_brothers.brother = receiver
                receiver.brother = sender
                relacion_establecida = True
                break
            ite_brothers = ite_brothers.brother
        if relacion_establecida:
            print("Relacion entre " + sender.nombre + " y " + receiver.nombre + " agregada.")
        else:
            print("Esta relacion ya fue agregada previamente.")
    else:
        sender.brother = receiver
        receiver.brother = sender
        print("Relacion entre " + sender.nombre + " y " + receiver.nombre + " agregada.")
