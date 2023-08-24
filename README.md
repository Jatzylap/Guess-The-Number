# Guess-The-Number
A small number guessing game concept.

# Controls
Use the mouse and number pad keys to play.

# Installation
To install the necessary library(ies) to run the script:

1- Open a console window (Terminal for Mac / CMD for Windows)

2- Change the current directory to the project path (cd path\to\project)

3- Install the libraries from the "requirements.txt" file using:

  ```
  pip install -r requirements.txt
  ```

# Pyinstaller (optional)
Use this command into CMD to compile into EXE for Windows OS
  ```
pyinstaller --noconsole -F --i "src/a/icon.ico" --add-data "src;src/"  "main.py"
  ```

## Development information
Developed by: Jatzylap

Libraries used: Pygame 2.5.0, OpenCV 4.8.0
