import functions

import PySimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter the todo", key="todo")
add_btn = sg.Button("Add")

window = sg.Window("My TO-DO-APP",
                   layout=[[[label], [input_box, add_btn]]],
                   font=('Helvetica', 20))
event = window.read()
print("Hi, event", event)





window.close()