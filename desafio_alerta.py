'''
    Desafio - Criar um automação que pede do usuário o seu email e a senha, logo depois copiar e colar em um bloco de notas simulando um página de login
'''

import pyautogui
from time import sleep
import pyperclip

# Mensagem informando que a automação teve inicio
pyautogui.alert(title='Automação', text='Automação iniciada!', button='OK')
# Pedir o email do usuário
email = pyautogui.prompt(title='Email', text='Digite o seu email: ')
if email != '': 
    pyautogui.alert(title='Informar email preenchido!', text='Email preenchido com sucesso!')
# Pedir a senha do usuário
senha = pyautogui.password(title='Senha', text='Digite a sua senha:', mask='*')
if senha != '':
    pyautogui.alert(title='Informar senha preenchida!', text='Senha preenchida com sucesso!')
# Abrir o bloco de notas
pyautogui.click(x=495, y=741, duration=1)
# Escrever o nome do bloco de notas
pyautogui.write('Bloco de notas', interval=0.2)
sleep(1)
pyautogui.press('enter')
# Mover o mouse até o local do bloco de notas
pyautogui.moveTo(x=689, y=243, duration=1)
# Copiar o email do usuário e colar no local do email
def copiar_email(email):
    pyperclip.copy(email)
    pyautogui.hotkey('ctrl', 'c')
copiar_email(email)
# write(email) também teria funcionado
pyautogui.hotkey('ctrl', 'v')
# Copiar a senha do usuário e colar no local da senha
pyautogui.press('enter')
sleep(1)
def copiar_senha(senha):
    pyperclip.copy(senha)
    pyautogui.hotkey('ctrl', 'c')
copiar_senha(senha)
# write(senha) também teria funcionado
pyautogui.hotkey('ctrl', 'v')