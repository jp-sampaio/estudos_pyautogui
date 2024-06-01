'''
    Alertar, informar, pedir dados do usuário e deixar a senha no formato de asterisco são maneiras interessantes de criar automações mais robustas e completas
'''

import pyautogui

# Mostrar uma mensagem para o usuário
# pyautogui.alert(title='Automação', text='Iniciando a automação', button='ok')

# Pedir alguma informações para o usuário
# email = pyautogui.prompt(title='Email', text='Informe o seu e-mail: ')
# print(email)

# Informar o usuário sobre alguma informação relevante como perguntar se ele deseja continuar com a automação
# resposta = pyautogui.confirm(title='Confirmação', text='Deseja continuar com a automação?', buttons=['Sim', 'Não', 'Cancelar'])
# print(resposta)

# Condicionarl para mostrar a utilização do confirm em uma aplicação
# if resposta == 'Sim':
#     print('Continuar a automação')
# elif resposta == 'Não':
#     print('Terminar a automação')
# else:
#     print('Cancelar a operação')


# Codificar uma mensagem no formato de * (asterisco) 
senha = pyautogui.password(title='Senha', text='Digite a sua senha:', mask='*')
print(f'Sua senha: {senha}')