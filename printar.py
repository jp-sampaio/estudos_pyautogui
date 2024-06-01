'''
    A maneira que temos para printar a tela é utilizando o screenshot, que pega os parâmetros, ponto inicial, distância a direita e distância para baixo
'''

import pyautogui

# Tirar um print do bloco de notas
pyautogui.screenshot('bloco de notas.jpg', region=(875, 131, 421, 436))