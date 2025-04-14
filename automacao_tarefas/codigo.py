import pyautogui
import time

# pyautogui.click -> clicar em algum lugar
# pyautogui.press -> apertar 1 tecla 
# pyautogui.write -> escrever um texto 
# pyautogui.hotkey -> apertar um combinação de teclas

pyautogui.PAUSE = 0.5

# Passo 1: Entrar no sistema da empresa - https://dlp.hashtagtreinamentos.com/python/intensivao/login
# abrir o chrome
pyautogui.press("win")
pyautogui.write("chrome")
pyautogui.press("enter")
pyautogui.click(x=418, y=372)

# digitar o site
#pyautogui.press("enter")
pyautogui.write(" https://dlp.hashtagtreinamentos.com/python/intensivao/login")
pyautogui.press("enter")

# espera 3 segundos
time.sleep(3)


# Passo 2: Fazer login
pyautogui.click(x=550, y=382)
pyautogui.write("ctrlmidias@gmail.com")
pyautogui.press("tab")
pyautogui.write("12345678")

# botao logar
pyautogui.press("tab")
pyautogui.press("enter")

# espera de 3 segundos
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
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
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
