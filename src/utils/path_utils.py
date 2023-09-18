def desktop_screen_path():
    base_path = "src/Locators_screen"
    doc_path = base_path + "/free_desktop/document.png"
    find_field = base_path + "/free_desktop/find_field.png"
    icon_btn = base_path + "/free_desktop/program_exe.png"
    path_list = {'base':base_path,'doc':doc_path,'find':find_field,'icon':icon_btn}
    return path_list

def login_page_screen():
    base_path = "src/Locators_screen"
    check_page = base_path + "/login_page/check_page.png"
    btn_login = base_path + "/login_page/btn_login.png"
    field_login = base_path + "/login_page/field_login.png"
    field_pass = base_path + "/login_page/field_pass.png"
    path_list = {'checkpage':check_page, 'btnlogin': btn_login, 'fieldlogin': field_login, 'fieldpass': field_pass}
    return path_list