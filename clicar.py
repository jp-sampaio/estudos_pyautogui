'''
    Personalizando os meus clicks, além de descobrir funções que possuem funcionalidades próprias
'''

import pyautogui

# A função click possuem alguns parâmetros que nos permitem personalizar ele 
pyautogui.click(x=300, y=500, clicks=5, interval=1, button='left', duration=2)

# Quando utilizamos somente a função sem nenhum parâmetro dentro, ele vai clicar nesse exato local
pyautogui.click()
pyautogui.click(button='left')
pyautogui.click(button='right')
pyautogui.click(button='middle')

# Funções definidas para determinadas funcionalidades
pyautogui.doubleClick()
pyautogui.tripleClick()
pyautogui.rightClick()
pyautogui.middleClick()