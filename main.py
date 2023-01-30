#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import signal
import pywinauto
from HandController import HandController


def open_notepad(event):
    event.print_line()
    print(event)
    try:
        app = pywinauto.application.Application().connect(path="notepad.exe")
    except pywinauto.application.ProcessNotFoundError:
        app = pywinauto.application.Application().start("notepad.exe")
        print("notepad is not open")
    app.Notepad.wait("visible")
    return app


def save_close_notepad(event):
    event.print_line()
    print(event)
    try:
        app = pywinauto.application.Application().connect(path="notepad.exe")
        app.Notepad.wait("visible")
        app.UntitledNotepad.Edit.type_keys("Hello World!")
        app.Notepad.menu_select("File -> Save")
        app.SaveAs.Edit.type_keys("test.txt")
        app.SaveAs.Save.click()
        app.Notepad.menu_select("File -> Exit")
    except pywinauto.application.ProcessNotFoundError:
        print("notepad is not open")


config = {
    'renderer': {'enable': True},

    'pose_actions': [
        {'name': '1_open_notepad', 'pose': 'FIST', 'hand': 'right', 'callback': 'open_notepad', "trigger": "enter_leave", "first_trigger_delay": 0.3},
        {'name': '2_close_save_notepad', 'pose': 'FIVE', 'hand': 'right', 'callback': 'save_close_notepad', "trigger": "enter_leave", "first_trigger_delay": 0.3},
    ]
}

HandController(config).loop()

# Manage ctrl+c to stop the program
signal.signal(signal.SIGINT, signal.SIG_DFL)
