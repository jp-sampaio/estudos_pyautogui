'''
    Utilizar o reconhecimento de imagem para descobrir as coordenadas de uma imagem 
'''

import pyautogui
from time import sleep

# Vai pedar as coordenadas x e y do centro da imagem
captcha = pyautogui.locateCenterOnScreen('image.png')
pyautogui.click(x=captcha[0], y=captcha[1], duration=2)
sleep(2)
pyautogui.click(935,522, duration=1)

# pyautogui.locateOnScreen pegar as coordenadas inicial e da direita, a altura e largura