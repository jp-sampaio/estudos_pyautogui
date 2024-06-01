'''
  Desafio - Entrar na página da wikipedia, rolar a página e acessar um link em um local especifico
'''
import pyautogui
from time import sleep

# Mover o mouse até ao campo para pesquisar sobre os apps do computador
pyautogui.click(x=535, y=745, clicks=1, interval=0, button='left', duration=1.5)
# Escrever o nome do navegador 
pyautogui.write('google chrome')
# Esperar um momento
sleep(0.5)
# Pressionar a tecla enter
pyautogui.press('enter')
# Pausa de 1 segundo para abrir o navegador
sleep(1)
# Direcionar o mouse até o campo de pesquisa
pyautogui.moveTo(x=241, y=58, duration=1)
pyautogui.click()
# Escrever o nome da Wikipedia
pyautogui.write('https://pt.wikipedia.org/wiki/Brasil')
# Esperar um momento
sleep(1)
# Pressionar a tecla enter
pyautogui.press('enter')
# Pausa de 2 segundos
sleep(2)
# Mover o mouse para o meio da página
pyautogui.moveTo(x=572, y=176, duration=1)
# Rolar a página até o local onde possa visualizar o link em questão
pyautogui.scroll(-2000)
# Mover o mouse até o local do link
pyautogui.moveTo(x=590, y=252, duration=1)
# Clicar no link
pyautogui.click()