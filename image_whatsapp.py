'''
    Automatizando um processo de enviar uma imagem via Whatsapp Web 
'''

import pyautogui
from time import sleep

# Procurar na barra de pesquisa do windows o app do whatsapp
pyautogui.click(x=521, y=742, clicks=1, interval=0, button='left', duration=1)

# Digitar o nome do whatsapp e clicar
pyautogui.write('whatsapp')
sleep(0.5)
pyautogui.press('enter')

# Esperar um momento até o app abrir
sleep(0.5)

# Abrir uma conversa que desejo enviar a imagem 
pyautogui.click(x=236, y=187, clicks=1, interval=0, button='left', duration=1)

sleep(0.5)

# Abrir o gerenciador de arquivos e entrar em documentos que é onde está a minha imagem
pyautogui.click(x=665, y=752, clicks=1, interval=0, button='left', duration=1)
pyautogui.click(x=110, y=355, clicks=1, interval=0, button='left', duration=1)

# Rolar a página até onde eu possa visualizar a imagem 
pyautogui.move(200, 0, duration=1)
pyautogui.scroll(-500)

# Mover o mouse até a imagem e segurar o clique
pyautogui.moveTo(x=281, y=529, duration=1) 
pyautogui.mouseDown()

# Mover até o ícone do whatsapp, esperar um pouco e depois arrastar até a conversa
pyautogui.moveTo(x=975, y=741, duration=1)
sleep(1)
pyautogui.move(0, -100)
pyautogui.mouseUp()
sleep(1)
pyautogui.write('Imagem de Teste')
pyautogui.press('enter')