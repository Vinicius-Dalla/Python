import pyautogui
from time import sleep

#1 - Navegar até o site do https://www.instagram.com/
import webbrowser
webbrowser.open_new_tab('https://www.instagram.com/')
'''
#2 - Entrar com usuário e senha.
pyautogui.click(1063,387,duration=1)
pyautogui.typewrite('vdzmello@gmail.com')

pyautogui.click(1050,435,duration=1)
pyautogui.typewrite('1503@Vini')
#3 - Clicar em login.
pyautogui.click(1183,498,duration=1)
sleep(3)

#4 - Clicar em Not now para não salvar navegador.
pyautogui.click(1079,641,duration=1)
sleep(1)
'''
#5 - Clicar no ícone do Instagram
pyautogui.click(107,191,duration=1)
sleep(1)
#6 - Pesquisar pela página.
pyautogui.click(98,356,duration=1)
#7 - Entrar na página.
pyautogui.typewrite('Nike')
sleep(1)
pyautogui.click(219,349,duration=1)
sleep(2)
#8 - Clicar na postagem mais recente.
pyautogui.click(673,848,duration=1)
sleep(2)
'''#9 - Verificar se já curtiu ou não a postagem.
coracao = pyautogui.locateCenterOnScreen('coracao.png')
sleep(3)
#10 - Se tiver curtido, fazer nada, e pausar o bot #por 24h.
if coracao is not None:
    sleep(86400)
#11 - Se não tiver curtido, curtir e comentar a foto.
elif coracao == None:
'''
pyautogui.click(980,821,duration=1)
sleep(1)
pyautogui.click(1055,953,duration=1)
pyautogui.typewrite('Very nice!')
pyautogui.press('Enter')
#12 - Pausar por 24h.
#sleep(86400)
#13 - Após 24h rodar o bot novamente.
