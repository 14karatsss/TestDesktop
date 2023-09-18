#Создание стартовых настроек ,а именно поиск и открытие самого приложения
import time
import pyautogui
import pytest
from src.utils.path_utils import desktop_screen_path

@pytest.fixture()
def set_up_app():
    all_path = desktop_screen_path()
    pyautogui.press('win')#открываю меню пуск
    btn_doc = pyautogui.locateOnScreen(all_path['doc'], confidence=0.8)#ищу кнопку проводника
    pyautogui.moveTo(btn_doc)
    pyautogui.click()#открываю проводиник
    i = 0
    while pyautogui.locateOnScreen(all_path['find']) == None and i <= 11: #ставлю таймер на открытие проводника
        time.sleep(0.5)
        i += 1

    btn_find_field = pyautogui.locateOnScreen(all_path['find'], confidence = 0.8)
    pyautogui.moveTo(btn_find_field)
    pyautogui.click()# кликаю в строку указания пути в проводнике

    pyautogui.write(r'C:\app_desktop', interval=0.15) #Открываем нужную папку
    pyautogui.press('enter')

    icon_app = pyautogui.locateOnScreen(all_path['icon'], confidence=0.8) #открываем приложение
    pyautogui.moveTo(icon_app)
    pyautogui.doubleClick()
    base_path = all_path['base']
    return base_path
