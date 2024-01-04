import PySimpleGUI as sg

lable1 = sg.Text("Select  file to compress", key="files")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")



lable2 = sg.Text("Select destination folder", key="folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

compress_button = sg.Button("compress")

layout = [
    [lable1, input1, choose_button1],
    [lable2, input2, choose_button2],
    [compress_button]
]
window = sg.Window("File compressor", layout=layout)

while True:
    event, values =window.read()
    print("Event", event, "Values", values)
    filePath = values["files"].split(";")
    folder = values["folder"]



window.close()

