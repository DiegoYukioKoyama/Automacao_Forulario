import pyautogui
import csv
import webbrowser
import time

#pausa entre os comandos do pyautogui.
pyautogui.PAUSE = 0.5

#abrir o formulário web e clicar no campo nome.
webbrowser.open('formulario.html')
time.sleep(2)
pyautogui.click(755,498)

#abrir a lista de nomes.
with open('lista_de_nomes.csv', 'r', encoding='utf-8') as arquivo:
    conteudo = csv.DictReader(arquivo)
    for linha in conteudo:

        #digita o nome no campo do formulário e passa para o próximo campo.
        pyautogui.write(linha['Nome'])
        pyautogui.press('tab')

        #digita o CPF no campo do formulário e passa para o próximo campo.
        pyautogui.write(linha['CPF'])
        pyautogui.press('tab')

        #digita o telefone no campo do formulário e clica no botão de envio.
        pyautogui.write(linha['Telefone'])
        pyautogui.press('tab')
        pyautogui.press('enter')
