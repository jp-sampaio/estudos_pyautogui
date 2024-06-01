'''
    A utilização do teclado é uma funcionalidade muito poderosa e excencial na construção de automações muito robustas
'''
import pyautogui

# Descobrir quais são as teclas com os seus respectivos nomes em inglês
print(pyautogui.KEYBOARD_KEYS)

# O hotkey faz a junção de duas ou mais teclas, como é o caso do control + c ou v
pyautogui.hotkey('ctrl' + 'v')

# Também em determinados casos posso fazer de forma individual com o keydown que segura a tecla e o keyup que solta
pyautogui.keyDown('alt')
pyautogui.keyUp('alt')

# A forma mais comum na utilização de um teclado que é pressionar uma tecla
pyautogui.press('space')