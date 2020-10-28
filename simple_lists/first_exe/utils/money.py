from utils.graphql import request_graph


def get_users(user_iterator):
    print(user_iterator.nombre)
    if user_iterator.next is None:
        return True
    get_users(user_iterator.next)


def main(current_user, base_todos):
    iterator_todos = base_todos
    while iterator_todos is not None:
        if iterator_todos.user_id == current_user.id:
            if current_user.todos is None:
                current_user.todos = iterator_todos
                continue

        iterator_todos = iterator_todos.next

    if current_user.next is not None:
        main(current_user.next, base_todos)

    return True


class Todo:
    id = 0
    id_user = 0
    contenido = 0
    estado = False
    next = None


class User:
    id = 0
    nombre = ""
    email = ""
    edad = ""
    next = None
    todos = None


users_dict = request_graph("users {id name age email }", "users")
todos_dict = request_graph("todos {id content isCompleted user { id }}", "todos")

u1 = User()
t1 = Todo()
users_base = u1
todos_base = t1

for todo in todos_dict:
    t1.id = int(todo["id"])
    t1.contenido = todo["content"]
    t1.estado = todo["isCompleted"]
    t1.id_user = int(todo["user"]["id"])
    previous = t1
    t1 = Todo()
    previous.next = t1

for user in users_dict:
    u1.id = int(user["id"])
    u1.nombre = user["name"]
    u1.edad = user["age"]
    u1.email = user["email"]
    previous = u1
    u1 = User()
    previous.next = u1

get_users(users_base)
# main(users_base, todos_base, None)
