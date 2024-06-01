'''
  Solicitar a rolagem de alguma página utilizando a função scroll;
'''


import pyautogui

# Mover o mouse até um local que devo mover o scroll
pyautogui.moveTo(x=1013, y=201, duration=1)

# Descer a página número negativo, subir é positivo e lembrando que é utilizado pixels
pyautogui.scroll(-3000)
