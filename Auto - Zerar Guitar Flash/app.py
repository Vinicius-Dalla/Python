import pyautogui
import keyboard
from time import sleep

pyautogui.click(1649,412,duration=1)
pyautogui.press('Enter')

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(1267,836,(12,152,33)):
        pyautogui.press('a')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1379,836,(254,15,23)):
        pyautogui.press('s')
        sleep(0.05)
    if pyautogui.pixelMatchesColor(1492,836,(244,244,64)):
        pyautogui.press('j')
        sleep(0.05)