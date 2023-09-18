from src.pages.LoginPage import LoginPage

def test_log_in(set_up_app):
    path = set_up_app #записываем базовый путь к скринам
    page = LoginPage(path) #Отправляем путь в для того чтобы на месте сделать локаторы
    status_load = page.check_load_login() #получаем статус загрузки приложения
    if status_load == None:
        raise Exception('Login page not loaded')# проверяем что приложение загрузилось и все элементы на месте
    main_page = page.do_login() # вводим логин и пароль и жмем кнопку войти
    status_load = main_page.check_load_page() #получаем новый статус загрузки главной страницы
    if status_load == None:
        raise Exception('Main page not loaded')#проверяем что все загрузилось
    main_page.logout() #выходим из приложения
    status_load = page.check_load_login()#получаем статус загрузки страницы авторизации
    if status_load == None:
        raise Exception('Login page not loaded')#проверяем что страница загрузилась успешно и все элементы есть
    page.close_program() #закрываем программу
