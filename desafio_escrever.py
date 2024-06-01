'''
    Desafio - Abrir o bloco de notas e escrever a frase "Automação é incrível!"
'''

import pyautogui
import pyperclip

def caracter_especial(frase):
    # Copia a frase já com os caracteres especiais
    pyperclip.copy(frase)
    # Utiliza o comando control + v para colar
    pyautogui.hotkey('ctrl', 'v')


# Mover o mouser até o campo de busca de apps
pyautogui.click(x=537, y=744, clicks=1, interval=0, button='left', duration=1)
# Escrever o nome do bloco de notas
pyautogui.write('bloco de notas', interval=0.2)
# Pressionar a tecla enter 
pyautogui.press('enter')
# Mover o mouse para o campo do bloco de notas
pyautogui.moveTo(x=806, y=218, duration=1)
# Escrever a frase proposta no desafio, nesse caso utilizando uma função que permite utilizar os caracter especial
caracter_especial('Automação é Incrível!')