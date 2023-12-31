import PySimpleGUI as sg

lable1 = sg.Text("Select  file to compress")
input1 = sg.Input()
choose_button1 = sg.FilesBrowse("Choose")



lable2 = sg.Text("Select destination folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

window = sg.Window("File compressor", layout=[
    [lable1, input1, choose_button1],
    [lable2, input2, choose_button2]
])

window.read()
window.close()

