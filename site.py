'''
    Maneira de como entrar em algum site e com isso automatizar ele, é uma alternativa já que o selenium é próprio para isso
'''

import webbrowser
# Abri uma nova janela do navegador padrão do windows
# webbrowser.open('google.com')

# Abri uma nova aba de um navegador padrão aberto
# webbrowser.open_new_tab('google.com')

# Abri uma nova janela
webbrowser.open_new('google.com')

# Em todos os casos se não tiver aberto, irá abrir o navegador e depois pode ser que ocorro o propósito de cada um