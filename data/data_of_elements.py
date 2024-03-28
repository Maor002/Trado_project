from selenium.webdriver.common.by import By

login_page = {
    "IL_button": (By.CLASS_NAME, 'languageChooser_languageChooserLtR'),
    "EN_button": (By.CLASS_NAME, 'languageChooser_languageChooser'),
    "element_phone": (By.XPATH, '//*[@id="root"]/div[1]/div[2]/div/span/form/div[1]/div/label'),
}