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

### Installation

1. Make sure to install the DepthAI libraries. Follow the instructions here https://docs.luxonis.com/en/latest/pages/tutorials/first_steps/.
2. Clone the repo.
3. Install the required packages using `pip install -r requirements.txt`.
    
    3.1 If you get the following error or something similar:
        
        ImportError: DLL load failed while importing win32ui: Error en una rutina de inicialización de biblioteca de vínculos dinámicos (DLL).
    
    You need to **install a new version of pywin32**, and also run the following command afterwards:

        python Scripts/pywin32_postinstall.py -install

## Usage

### Running the application

1. Connect OAK-D Lite to the computer.
3. Run the `main.py` file.

### References

- [1] https://github.com/geaxgx/depthai_hand_tracker
- [2] https://github.com/pywinauto/pywinauto

