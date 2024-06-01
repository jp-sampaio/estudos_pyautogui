'''
    Escrever com a função write, que nos auxilia em digitar textos em diferentes locais 
'''

import pyautogui
import pyperclip
from time import sleep

# Função que permite utilizar os caracteres especiais
def caracteres_especiais(frase):
    pyperclip.copy(frase)
    pyautogui.hotkey('ctrl', 'v')
    sleep(1)

# Mover o mouser até o campo de busca de apps
pyautogui.click(x=537, y=744, clicks=1, interval=0, button='left', duration=1)
# Escrever o nome do whatsapp
pyautogui.write('whatsapp', interval=0.2)
# Pressionar o botão enter
pyautogui.press('enter')
# Entrar na conversa que desejo escrever uma mensagem
pyautogui.moveTo(x=219, y=187, duration=1)
pyautogui.click()
# Mover o mouse até o campo de escrever 
pyautogui.click(x=597, y=694, clicks=1, interval=0, button='left', duration=1)
# Escrever a mensagem que quero enviar
caracteres_especiais('Olá, bom dia!')
# Pressionar a tecla enter para enviar a mensagem
pyautogui.press('enter')