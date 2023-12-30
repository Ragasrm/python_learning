# imports
from functions import get_todos, write_todos

# program starts here..!
while True:
    user_action = input("Type add or show or edit or complete or exit:").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        todos = get_todos()
        todos.append(todo + '\n')
        write_todos(todos)

    elif user_action.startswith("show"):
        todos = get_todos()
        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f"{index + 1}-{todo}"
            print(row)

    elif user_action.startswith("edit"):
        try:
            number = int(user_action[5:])
            number = number - 1

            todos = get_todos()

            new_todo = input("Enter new todo to replace  " + todos[number].strip('\n') + ":").strip()
            todos[number] = new_todo + '\n'

            write_todos(todos)
        except ValueError:
            print("your commend is not valid")
            continue

    elif user_action.startswith("complete"):
        try:
            number = int(user_action[9:])

            todos = get_todos()

            index = number - 1
            todo_to_remove = todos[index].strip("\n")
            todos.pop(index)
            write_todos(todos)
            message = f"Todo {todo_to_remove} was removed from the list"
            print(message)
        except IndexError:
            print("the index is not found..!")
            continue

    elif user_action.startswith("exit"):
        break
    else:
        print("comment is not valid..!")
print('Bye..!')
