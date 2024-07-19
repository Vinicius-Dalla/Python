import pyautogui
from time import sleep 
import webbrowser

# Abrir site
webbrowser.open_new_tab('https://cursoautomacao.netlify.app/')
# Clicar no site
pyautogui.click(479,239,duration=1)
#Rolar a página até o campo de alerta
pyautogui.scroll(-2000)
sleep(1)
#CLicar no campo de nome
pyautogui.click(119,735,duration=1)
# Escrever meu nome
pyautogui.typewrite('Vinicius Dalla')
#Clicar no botão alerta
pyautogui.click(93,774,duration=1)
#Clicar em fechar o alerta
pyautogui.click(699,236,duration=1)
#Subir página do site
pyautogui.scroll(2000)
# Descer a página até os arquivos
pyautogui.scroll(-3600)
#Clicar nos arquivos de Excel e PDF para download
pyautogui.click(240,572,duration=1)
pyautogui.click(263,715,duration=1)
#Criar alerta "VOCÊ TERMINOU"
pyautogui.alert('VOCÊ TERMINOU')






