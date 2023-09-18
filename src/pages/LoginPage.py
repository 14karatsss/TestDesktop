import pyautogui
import time
import os
from dotenv import load_dotenv
from src.pages.MainPage import MainPage
from src.utils.path_utils import login_page_screen

class LoginPage:

    def __init__(self, path):

        self.path = path #получаю путь к скринам
        self.base_path = path + "/login_page" # добавляю в путь шаг чтобы использовать папку соответствующую для этой страницы
        self._check_page_png = self.base_path + "/check_page.png" #прописываю скрин который хочу использовать
        self._check_page_locator = pyautogui.locateOnScreen(self._check_page_png, confidence = 0.8) #готовый локатор

        self._all_path = login_page_screen()#вызываю функцию которая предоставит все пути заранее прописанные в отдельном файле
        #self._login_field = self.base_path + "/field_login.png"
        self._login_field_locator = pyautogui.locateOnScreen(self._all_path['fieldlogin'], confidence = 0.8)#сразу создаю локатор

        self._login_field2 = self.base_path + "/field_login_v2.png" #использование не прямого локатора а именно пути скрина, а сам поиск делать в методах
        self._pass_field = self.base_path + "/field_pass.png"
        self._login_btn = self.base_path + "/btn_login.png"
        self._close_btn = self.base_path + "/close_btn.png"
        self._confirm_close = self.base_path + "/confirm_close.png"

    def check_load_login(self):
        i = 0
        while self._check_page_locator == None and i <= 11:
            time.sleep(1)
            i += 1

        status_page_load = pyautogui.locateOnScreen(self._check_page_png, confidence = 0.8)

        return status_page_load

    def write_login(self):
        load_dotenv()
        login = os.getenv("LOGIN")
        if self._login_field_locator == None:
            login_field = pyautogui.locateOnScreen(self._login_field2, confidence = 0.8)
            pyautogui.moveTo(login_field)
            pyautogui.click()
            pyautogui.hotkey('ctrl', 'a', interval=0.25)
            pyautogui.press('backspace')
        else:
            login_field = self._login_field_locator
            pyautogui.moveTo(login_field)
            pyautogui.click()
        pyautogui.write(login, interval = 0.1)

    def write_password(self):
        load_dotenv()
        password = os.getenv("PASSWORD")
        password_field = pyautogui.locateOnScreen(self._pass_field, confidence = 0.8)
        pyautogui.moveTo(password_field)
        pyautogui.click()
        pyautogui.write(password, interval=0.1)

    def press_login_btn(self):
        loginbtn = pyautogui.locateOnScreen(self._login_btn, confidence = 0.8)
        pyautogui.click(loginbtn)

    def do_login(self):
        self.write_login()
        self.write_password()
        self.press_login_btn()
        return MainPage(self.path)

    def close_program(self):
        close_btn = pyautogui.locateOnScreen(self._close_btn, confidence = 0.8)
        pyautogui.click(close_btn)
        i = 0
        while pyautogui.locateOnScreen(self._confirm_close, confidence=0.8) == None and i <= 11:
            time.sleep(0.5)
            i += 1
        confirm_close = pyautogui.locateOnScreen(self._confirm_close, confidence = 0.9)
        pyautogui.moveTo(confirm_close)
        pyautogui.click()







