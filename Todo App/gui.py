import functions

import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter the todo", key="todo")
add_btn = sg.Button("Add")

window = sg.Window("My TO-DO-APP",
                   layout=[[label], [input_box, add_btn]],
                   font=('Helvetica', 20))

while True:
    event, values = window.read()
    print("Hi, event", event)
    match event:
        case "Add":
            todos = functions.get_todos()
            print("todos", todos)
            new_todo = values['todo'] + '\n'
            todos.append(new_todo)
            functions.write_todos(todos)
window.close()