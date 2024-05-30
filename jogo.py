"""
    Aprendendo a mover o mouse e clicar em um determinado local
"""
import pyautogui
from time import sleep

# Entrar no navegador onde está o jogo
# O moveTo utiliza as coordenadas x e y para mover o mouse até essa posição, já o duration é o tempo que demora;
pyautogui.moveTo(912,744, duration=2)
pyautogui.click()

# Mover até a pedra 
pyautogui.moveTo(487,397, duration=2)
pyautogui.move(10, 0, duration=0.1)

# Move utilizando pixels como parâmetro, podendo ser positivo ou negativo;
# pyautogui.move(30,-12, duration=0.1)

# Loop pra clicar várias vezes
# Esse parâmetro serve para clicar, e o clique ocorre onde o mouse está parado no momento que é chamado
for i in range(62):
    sleep(0.3)
    pyautogui.click()