'''
    A funcionalidade de arrastar é muito importante nas automações
'''

import pyautogui


# Passos para arrastar os arquivos para outra pasta
# Passo 1 - Mover o mouse e clicar no gerenciador de arquivo que possui pastas mescladas
pyautogui.click(x=680, y=743, clicks=1, interval=0, button='left', duration=1)

# Passo 2 - Mover o mouse até a primeira pasta e clicar nela, depois repetir o processo com a próxima
pyautogui.click(x=841, y=640, clicks=1, interval=0, button='left', duration=1)
pyautogui.click(x=680, y=743, clicks=1, interval=0, button='left', duration=1)

# Passo 3 - Mover o mouse até a segunda pasta e clicar nela
pyautogui.click(x=741, y=640, clicks=1, interval=0, button='left', duration=1)

# Passo 6 - Fazer o loop com a quantidade de pasta que preciso arrastar
for i in range(11):
    # Passo 4 - Mover o mouse até o posição do primeiro arquivo 
    pyautogui.moveTo(x=234, y=183, duration=1)

    # Passo 5 - Arrastar o arquivo até a próxima pasta
    pyautogui.dragTo(x=1327, y=637, button='left', duration=1) # Clica, arrasta e solta na posição que foi declarada

    