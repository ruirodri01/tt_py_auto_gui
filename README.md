# PyAutoGUI Automation Script Example

This repository contains a Python script that automates some tasks on a Windows machine using the PyAutoGUI library. 

## Features

- Opens Notepad using `Win + R` and types the current date and time.
- Takes screenshots of the Notepad window and saves them with a timestamp in the `screenshots/` folder.
- Closes Notepad without saving the file.
- Interacts with the Start button by identifying its location using an image match.
- Takes another screenshot of the Start menu and saves it with a timestamp.
- Prints a message to the console indicating the success of the operation.

## Prerequisites

Before you can install and run the script, ensure the following tools are installed on your system:

1. **Python 3.x**: Ensure Python is installed on your system. You can download the latest version from the [official Python website](https://www.python.org/downloads/).
    - Verify the installation by running:
      ```bash
      python --version
      ```

2. **Pip**: Pip, the Python package installer, is usually bundled with Python. If not, you can install it by following the instructions [here](https://pip.pypa.io/en/stable/installation/).

3. **Virtual Environment**: Ensure that `venv` is available to create virtual environments. It comes by default with Python 3.x.

## Installation

1. Clone the repository:
    ```bash
    git clone https://github.com/ruirodri01/tt_py_auto_gui.git
    ```

2. Navigate to the project directory:
    ```bash
    cd tt_py_auto_gui
    ```

3. Create and activate a virtual environment:
   - **For Windows:**
     ```bash
     python -m venv venv
     venv\Scripts\activate.bat
     ```
   - **For macOS/Linux:**
     ```bash
     python3 -m venv venv
     source venv/bin/activate
     ```

4. Install the required dependencies:
    ```bash
    pip install -r requirements.txt
    ```

5. Ensure that the following folders exist:
    - `screenshots/`: This folder is used to store screenshots taken by the script.
    - `images/`: This folder should contain the image `iniciar.png`, which is used to identify the Start button.

## Usage
To run the script, simply execute it using Python:

  ```bash
  python py_auto_gui.py
  ```

## Make sure that:
* Your screen resolution matches the one used to create the iniciar.png image for accurate image recognition.
* The images and screenshots directories are correctly set up.

## Exiting the Virtual Environment<br>
Once you're done, you can deactivate the virtual environment by running:<br>
    
  ```bash
  deactivate
  ```
## Notes
* You might need to adjust the time delays (pag.sleep(wait)) depending on the performance of your machine.
* Ensure that the iniciar.png image matches the Start button on your screen to avoid issues with locating the Start menu.
