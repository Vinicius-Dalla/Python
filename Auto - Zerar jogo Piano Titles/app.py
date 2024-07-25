import pyautogui
import keyboard
import win32api
import win32con
from time import sleep

pyautogui.click(519,553, duration=1)

def click(x, y):
    win32api.SetCursorPos((x, y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0)
    sleep(0.05)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

while keyboard.is_pressed('1') == False:
    if pyautogui.pixelMatchesColor(365,441, (0, 0, 0)):
        click(365,441)
    if pyautogui.pixelMatchesColor(472,439, (0, 0, 0)):
        click(472,439)
    if pyautogui.pixelMatchesColor(574,438, (0, 0, 0)):
        click(574,438)
    if pyautogui.pixelMatchesColor(685,437, (0, 0, 0)):
        click(685,437)