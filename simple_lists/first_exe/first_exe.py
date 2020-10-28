from simple_lists.first_exe.utils import edad, person, http, roles


def main():
    base = None
    lista_personas = http.GET_request('https://jsonplaceholder.typicode.com/users')
    opt = -1
    while opt != 10:
        print("====================================")
        print("               M E N U              ")
        print("====================================")
        print("1. Llenar lista de gente.             ")
        print("2. Obtener promedios de hombres y mujeres.")
        print("3. Listar                           ")
        print("4. Obtener roles duplicados         ")
        print("5. ¿Esta la lista ordenada por rol? ")
        print("6. Eliminar la lista                ")
        print("7. Agregar brother                  ")
        print("8. Obtener informacion de usuario por rol.")
        print("9. Eliminar usuario por rol.")
        print("10. Salir                            ")
        print("====================================")
        opt = int(input("Ingrese opcion: "))
        if opt == 1:
            for i in range(10):
                base = person.agregar_persona(base, lista_personas[i])
        if opt == 2:
            edad.print_promedio_edad(base)
        if opt == 3:
            person.listar_personas(base)
        if opt == 4:
            roles_cantidad = roles.get_roles_comunes(base)
            roles.print_roles_repetidos(roles_cantidad)
        if opt == 5:
            roles.print_esta_ordenada_por_roles(base)
        if opt == 6:
            base = None
        if opt == 7:
            sender = int(input("Hermano 1: "))
            receiver = int(input("Hermano 2: "))
            person.add_brother(base, sender, receiver)
        if opt == 8:
            rol = int(input("Ingrese rol de persona a buscar: "))
            if person.listar_persona(base, rol) is None:
                print("Persona no encontrada")
        if opt == 9:
            rol = int(input("Ingrese rol de persona a eliminar: "))
            base = person.eliminar_persona(base, rol)
        input("Enter para continuar...")
