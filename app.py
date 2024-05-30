'''
    O pyautogui serve para pegar as coordenadas de uma tela e fazer as automações com base nelas
'''

import pyautogui
from mouseinfo import mouseInfo

# O position informa onde o mouse está naquele exato momento, e caso eu venha mudar de lugar, o valor altera.
# posicao_estatica = pyautogui.position()
# print(posicao_estatica)

# Enquanto eu vou mudando o mouse de lugar o valor vai se alterando juntamente, também é mostrado a cor em rgb.
# posicao_dinamica = pyautogui.displayMousePosition()
# print(posicao_dinamica)

# O mais indicado seria utilizar o mouseinfo, que pode pegar mais de uma posição do mouse de uma vez.
mouseInfo()