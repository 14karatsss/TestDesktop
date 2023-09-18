import time

import pyautogui


class MainPage:
    def __init__(self,path):
        self.path = path
        self.base_path = path + "/main_page"
        self._check_load_mp = self.base_path + "/load_main_page.png"
        self._btn_logout = self.base_path + "/btn_exit.png"
        self._check_logout = self.path + "/login_page/check_page.png"

    def check_load_page(self):
        i = 0
        while pyautogui.locateOnScreen(self._check_load_mp, confidence=0.8) == None and i <= 11:
            time.sleep(1)
            i += 1

        status_page_load = pyautogui.locateOnScreen(self._check_load_mp, confidence=0.8)

        return status_page_load

    def logout(self):
        btn_logout = pyautogui.locateOnScreen(self._btn_logout,confidence=0.8)
        pyautogui.click(btn_logout)

    def check_logout(self):
        i = 0
        while pyautogui.locateOnScreen(self._check_logout, confidence = 0.8) == None and i <= 11:
            time.sleep(1)
            i += 1

        status_page_load = pyautogui.locateOnScreen(self._check_logout, confidence = 0.8)

        return status_page_load
