import time

from selenium.webdriver import Keys
from selenium.webdriver.common.by import By

from data.data_of_elements import *


def get_login(actions):
    my_dict = {}
    button_en = actions.find_element(login_page.get("EN_button"))
    actions.click_element(button_en)
    time.sleep(2)
    text = actions.get_text(login_page.get("element_phone"))
    my_dict["EN"] = text
    button_en = actions.find_element(login_page.get("IL_button"))
    actions.click_element(button_en)
    time.sleep(2)
    text = actions.get_text(login_page.get("element_phone"))
    my_dict["IL"] = text
    return my_dict


