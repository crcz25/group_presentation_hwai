# group_presentation_hwai
Hardware Acceleration for AI - Group Presentation

## Group Members

- Carlos Cueto
- Henry Ascencio
- Vasista 
- Aman 

## Installation and Setup

### Prerequisites

- Python >= 3.9
- opencv-python >= 4.5.1.48
- depthai>=2.13
- pywinauto >= 0.6.8
- Pillow >= 8.2.0
- Windows 10 (right now only win32 apps are supported)

### Installation

1. Make sure to install the DepthAI libraries. Follow the instructions here https://docs.luxonis.com/en/latest/pages/tutorials/first_steps/.
2. Clone the repo.
3. Install the required packages using `pip install -r requirements.txt`.
    
    3.1 If you get the following error or something similar:
        
        ImportError: DLL load failed while importing win32ui: Error en una rutina de inicialización de biblioteca de vínculos dinámicos (DLL).
    
    You need to **install a new version of pywin32**, and also run the following command afterwards:
        
        $ pip uninstall pywin32

        $ pip install pywin32

        $ python Scripts/pywin32_postinstall.py -install

## Usage

### Running the application

1. Connect OAK-D Lite to the computer.
3. Run the `main.py` file as follows:

        python main.py
3. To open notepad, raise your right hand and make a fist in front of the OAK-D camera.
4. To write *HelloWorld!* in the notepad, raise your right hand and make a five in front of the OAK-D camera.


## Open Notepad with Hand Gesture
![open_notepad](https://user-images.githubusercontent.com/31625277/215558475-bfc38229-a5d9-47f1-a88c-4809fab27b26.gif)


## Write *HelloWorld!* in Notepad with Hand Gesture
![write_notepad](https://user-images.githubusercontent.com/31625277/215558505-fd0f0b57-403d-414d-8199-614359c43d75.gif)


## Complete functionality 
![both](https://user-images.githubusercontent.com/31625277/215558526-60b3051a-ee98-40d3-84cd-d15db03d24d4.gif)


### References

- [1] https://github.com/geaxgx/depthai_hand_tracker
- [2] https://github.com/pywinauto/pywinauto

