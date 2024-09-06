import pyautogui as pag
import datetime

# Set the wait time between actions in seconds
wait=2

# Open the Windows Run dialog
pag.hotkey("win", "r")

# Type the name of the program to run
pag.typewrite("notepad")

# Press Enter to open the program
pag.press("enter")

# Wait for the program to load
pag.sleep(wait)

# Write the current time into the notepad
pag.typewrite(f"The time now is {datetime.datetime.now()}\n")

# Take a screenshot of the notepad window
now = datetime.datetime.now().strftime("screenshots/shot-%Y-%m-%d_%H-%M-%S-%f-01.png")
pag.screenshot(now)

# Close the notepad window
pag.hotkey("alt", "f4")
pag.sleep(wait)

# Select "No" to do not save the changes
pag.hotkey("alt", "n")

# Localiza o centro do botão "Iniciar" na tela
startButton = pag.locateCenterOnScreen('images/iniciar.png')

# Move o mouse para esta posição
pag.moveTo(startButton)

# Clique no botão "Iniciar"
pag.click()

# Espera o tempo configurado 
pag.sleep(wait)

# Tira um print da tela
now = datetime.datetime.now().strftime("screenshots/shot-%Y-%m-%d_%H-%M-%S-%f-02.png")
pag.screenshot(now)

# Manda um esc
pag.press("esc")

# Imprime "e aí, funcionou?"
print("\ne aí, funcionou? :D\n")

