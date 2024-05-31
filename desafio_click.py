import pyautogui
from time import sleep

# Entrar no meu gerenciador de arquivos, especificamente na área de trabalho;
pyautogui.click(x=733, y=740, clicks=1, interval=0, button='left', duration=2)

# Ir com mouse para um espaço vazio, provavelmente no meio;
pyautogui.move(0, -400, duration=2)

# Clicar com o botão direito;
pyautogui.rightClick()

# Ir até na opção novo;
pyautogui.click(x=802, y=470, clicks=1, interval=0, button='left', duration=2)

# Ir até na opção pasta;
pyautogui.click(x=1152, y=464, clicks=1, interval=0, button='left', duration=2)

# Escrever o nome da pasta
pyautogui.write('outra pasta teste')
pyautogui.press('enter')