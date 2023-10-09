# Passo a passo do projeto
# Passo 1: Entra no sistema da empresa
# https://dlp.hashtagtreinamentos.com/python/intensivao/login

import pandas as pd  # pip install pandas numpy openpyxl
import pyautogui  # Para instalar: pip install pyautogui
import time

# pyautogui.write -> escrever um texto
# pyautogui.press -> apertar 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> combinação de teclase

pyautogui.PAUSE = 0.5

# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")

# entrar no link
linkh = "https://dlp.hashtagtreinamentos.com/python/intensivao/login"
pyautogui.write(linkh)
pyautogui.press("enter")


# esperar o site carregar
time.sleep(3)

# Passo 2: Fazer login
# Click no campo de email
pyautogui.click(x=393, y=398)
pyautogui.write("tiagommpro@gmail.com")  # escrever o seu email

pyautogui.press("tab")  # passando pro próximo campo de senha
pyautogui.write("123456")

pyautogui.press("tab")  # passando pro próximo campo
pyautogui.press("enter")  # Entrando no sistema

time.sleep(3)

# Passo 3: Importar a base de dados de produtos
tabela = pd.read_csv("produtos.csv")

print(tabela)

for linha in tabela.index:
    # Passo 4: Cadastrar 1 produto
    pyautogui.click(x=389, y=278)

    # Preencher os campos
    pyautogui.write(str(tabela.loc[linha, "codigo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")

    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")

    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(obs))

    # Clicar para enviar
    pyautogui.press("tab")
    pyautogui.press("enter")

    pyautogui.scroll(50000)

# Passo 5: Repetir o cadastro para todos os produtos
