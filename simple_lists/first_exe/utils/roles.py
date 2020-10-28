def get_roles_comunes(base):
    it_roles = base
    roles = {}
    while it_roles is not None:
        if it_roles.rol not in roles:
            roles[it_roles.rol] = 1
        else:
            roles[it_roles.rol] += 1
        it_roles = it_roles.next
    if base is not None:
        return roles
    else:
        return None


def print_roles_repetidos(roles):
    hay_duplicados = False
    if roles is None:
        print("No hay gente aun!!")
    else:
        for rol_key in roles:
            actual_rol = roles[rol_key]
            if actual_rol > 1:
                hay_duplicados = True
                print("El rol numero " + str(rol_key) + " tiene " + str(actual_rol) + " personas.")
        if not hay_duplicados:
            print("No hay roles duplicados")


def print_esta_ordenada_por_roles(base):
    is_ordenada = True
    roles = get_roles_comunes(base)  # {"rol": n° usuarios, ...}
    if roles is None:
        print("No hay usuarios aun...")
    ite_roles = base
    while ite_roles is not None:
        actual_rol = ite_roles.rol
        
    if is_ordenada:
        print("Está ordenada por roles!")
    else:
        print("No está ordenada por roles")
