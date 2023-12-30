def get_todos(filepath='todos.txt'):
    """ Read the text file and return to-do items"""
    with open(filepath, 'r') as file_local:
        todos_local = file_local.readlines()
    return todos_local


def write_todos(todos_items, filepath='todos.txt'):
    """ write the to-do items in text file"""
    with open(filepath, 'w') as file:
        file.writelines(todos_items)

