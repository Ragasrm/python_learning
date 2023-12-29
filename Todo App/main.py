while True:
    user_action = input("Type add or show or edit or complete or exit:").strip()

    if user_action.startswith("add"):
        todo = user_action[4:]
        with open('todos.txt','r') as file:
            todos = file.readlines()
        todos.append(todo + '\n')
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif user_action.startswith("show"):
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()
        #new_todos = [item.strip('\n') for item in todos]
        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f"{index + 1}-{todo}"
            print(row)
    elif user_action.startswith("edit"):
        number = int(user_action[5:])
        number = number - 1

        with open('todos.txt','r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo to replace  " + todos[number].strip('\n') + ":").strip()
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif user_action.startswith("complete"):
        number = int(user_action[9:])

        with open('todos.txt', 'r') as file:
            todos = file.readlines()
        index = number - 1
        todo_to_remove = todos[index].strip("\n")
        todos.pop(index)

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

        message = f"Todo {todo_to_remove} was removed from the list"
        print(message)
    elif user_action.startswith("exit"):
        break
    else:
        print("comment is not valid..!")
print('Bye..!')
