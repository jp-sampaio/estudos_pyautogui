'''
    DESAFIO 🥇
    1) Navegue até o site https://cursoautomacao.netlify.app/
    2) Encontre e clique no campo "Digite seu nome" dentro de "exemplos Alertas" e digite seu nome
    3) Clique em alerta, para gerar a alerta
    4) Feche a alerta
    5) Suba a página totalmente para cima
    6) Desça apenas o suficiente para conseguir chegar até a secção que contém os arquivos para o quais irá fazer o download e click no botão de download para realizar o downlaod dos arquivos excel e pdf.
    7) Depois de ter feito isso, crie uma alerta que diz "VOCÊ TERMINOU"
'''

import webbrowser
import pyautogui
import pyperclip
from time import sleep

url = 'https://cursoautomacao.netlify.app/'

def escrever_nome(nome):
    pyperclip.copy(nome)
    pyautogui.hotkey('ctrl', 'v')

webbrowser.open(url)
sleep(3.3)

pyautogui.scroll(-1000)
sleep(1.5)

campo_nome = pyautogui.locateCenterOnScreen('campo_nome.png')
pyautogui.click(x=campo_nome[0], y=campo_nome[1], duration=1.6)
escrever_nome('João Paulo')
sleep(1.3)
pyautogui.press('tab')
sleep(1)
pyautogui.press('enter')
sleep(2)
pyautogui.press('enter')
sleep(1)

pyautogui.scroll(2000)
sleep(0.5)
pyautogui.scroll(-2100)

pyautogui.click(x=207, y=320, duration=1.7)
sleep(1.9)
pyautogui.click(x=407, y=319, duration=1.4)
sleep(3)

pyautogui.alert(title='Warning', text='VOCÊ TERMINOU!')