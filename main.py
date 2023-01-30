#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# Import required modules
import signal
import pywinauto
import time

from HandController import HandController

# Get the current date
today = time.strftime("%d-%m-%Y")

# Function to open Notepad
def open_notepad(event):
    # Print event information
    event.print_line()
    print(event)
    try:
        # Try to connect to an instance of Notepad
        app = pywinauto.application.Application().connect(path="notepad.exe")
    except pywinauto.application.ProcessNotFoundError:
        # If connection fails, start a new instance of Notepad
        app = pywinauto.application.Application().start("notepad.exe")
        print("notepad is not open")
    # Wait for Notepad to be visible
    app.Notepad.wait("visible")
    # Return the Notepad app object
    return app

# Function to save and close Notepad
def save_close_notepad(event):
    # Print event information
    event.print_line()
    print(event)
    try:
        # Try to connect to an instance of Notepad
        app = pywinauto.application.Application().connect(path="notepad.exe")
        # Wait for Notepad to be visible
        app.Notepad.wait("visible")
        # Type "Hello World!" in Notepad
        app.UntitledNotepad.Edit.type_keys("Hello World!")
        # Save the file and close Notepad
        app.Notepad.menu_select("File -> Save")
        # Type the file name
        app.SaveAs.Edit.type_keys(f"test_{today}.txt")
        # Save the file
        app.SaveAs.Save.click()
        # Close Notepad
        app.Notepad.menu_select("File -> Exit")
    except pywinauto.application.ProcessNotFoundError:
        # If connection fails, print a message
        print("notepad is not open")


# Define the configuration for the HandController
config = {
    'renderer': {'enable': True},

    'pose_actions': [
        {'name': '1_open_notepad', 'pose': 'FIST', 'hand': 'right',
            'callback': 'open_notepad', "trigger": "enter_leave", "first_trigger_delay": 0.3},
        {'name': '2_close_save_notepad', 'pose': 'FIVE', 'hand': 'right',
            'callback': 'save_close_notepad', "trigger": "enter_leave", "first_trigger_delay": 0.3},
    ]
}

# Create a HandController object
HandController(config).loop()

# Manage ctrl+c to stop the program
signal.signal(signal.SIGINT, signal.SIG_DFL)
