import PySimpleGUI as sg


def show_popup(status, title, message) -> object:
    if status == 0:
        sg.Popup(title, message)
    elif status == 1:
        sg.PopupError(title, message+"\n")
