#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pywinauto
from HandController import HandController

def open_notepad(event):
    event.print_line()
    print(event)
    try:
        app = pywinauto.application.Application().connect(path="notepad.exe")
        print("notepad is already open")
    except pywinauto.application.ProcessNotFoundError:
        app = pywinauto.application.Application().start("notepad.exe")
        print("notepad is not open")
    app.Notepad.wait("visible")
    return app

def trace(event):
    event.print_line()

def trace_rotation(event):
    event.print_line() 
    print("Rotation:", event.hand.rotation) 

def trace_index_finger_tip(event):
    event.print_line() 
    x, y = event.hand.landmarks[8,:2]
    print(f"Index finger tip : x={x}  y={y}") 

config = {
    'renderer' : {'enable': True},
    
    'pose_actions' : [
        {'name': '1_right_enter', 'pose':'ONE', 'hand':'right', 'callback': 'trace',"trigger":"enter", "first_trigger_delay":0.3},
        {'name': '2_right_enter_leave', 'pose':['TWO','PEACE'], 'hand':'right', 'callback': 'trace',"trigger":"enter_leave"},
        # To open notepad, the fist must be in the pose for at least 0.3 seconds
        {'name': '1_open_notepad', 'pose':'FIST', 'hand':'right', 'callback': 'open_notepad', "trigger":"enter_leave", "first_trigger_delay":0.3},

        # {'name': '3_right_periodic_1s', 'pose':'THREE', 'hand':'right', 'callback': 'trace', "trigger":"periodic", "first_trigger_delay":0, "next_trigger_delay": 1},
        # {'name': '4_right_periodic_0.3s', 'pose':'FOUR', 'hand':'right', 'callback': 'trace', "trigger":"periodic", "first_trigger_delay":0, "next_trigger_delay": 0.3},
        # {'name': '5_periodic_rotation', 'pose':'FIVE', 'callback': 'trace_rotation', "trigger":"periodic", "first_trigger_delay":0, "next_trigger_delay": 0.2},
        # {'name': '1_left_continuous_xy', 'pose':'ONE', 'hand':'left', 'callback': 'trace_index_finger_tip',"trigger":"continuous"},
    ]
}

HandController(config).loop()