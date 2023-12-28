while True:
    user_action = input("Type add or show or edit or complete or exit:").strip()

    if 'add' in user_action:
        todo = user_action[4:] + '\n'
        with open('todos.txt','r') as file:
            todos = file.readlines()
        todos.append(todo)
        with open('todos.txt', 'w') as file:
            file.writelines(todos)
    elif 'show' in user_action:
        file = open('todos.txt', 'r')
        todos = file.readlines()
        file.close()
        #new_todos = [item.strip('\n') for item in todos]
        for index, todo in enumerate(todos):
            todo = todo.strip('\n')
            row = f"{index + 1}-{todo}"
            print(row)
    elif 'edit' in user_action:
        number = int(user_action[5:])
        number = number - 1

        with open('todos.txt','r') as file:
            todos = file.readlines()

        new_todo = input("Enter new todo to replace  " + todos[number].strip('\n') + ":").strip()
        todos[number] = new_todo + '\n'

        with open('todos.txt', 'w') as file:
            file.writelines(todos)

    elif 'complete' in user_action:
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
    elif 'exit' in user_action:
        break
    else:
        print("comment is not valid..!")
print('Bye..!')
