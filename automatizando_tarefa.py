pip install yfinance
pip install matplotlib
pip install pyautogui
pip install pyperclip


import yfinance
import matplotlib
ticker = input("Digite a sigla da ação desejada: ")
dados = yfinance.Ticker(ticker).history("6mo")
fechamento = dados.CLOSE
fechamento.plot()
minima = fechamento.min()
maxima = fechamento.max()
atual = fechamento[-1]

import pyautogui
import pyperclip
pyautogui.PAUSE = 2
pyautogui.hotkey("ctrl","t")
pyperclip.copy("www.gmail.com")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("enter")
pyautogui.click(x=170, y=302)

pyperclip.copy("douglasbruzon10@gmail.com")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

pyperclip.copy("Análises diárias")
pyautogui.hotkey("ctrl","v")
pyautogui.hotkey("tab")

mensagem = f""" Prezado Gestor 
 Segue as análises dos últimos seis meses da ação {ticker}:
 Cotação máxima: R${round(maxima, 2)}
 Cotação mínima: R${round(minima, 2)}
 Cotação atual : R${round(atual, 2)}

Qualquer dúvida estou à disposição!

Att,
 """
pyperclip.copy(mensagem)
pyautogui.hotkey("ctrl","v")
pyautogui.click(x=1146, y=1036)
