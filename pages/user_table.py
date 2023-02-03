from selenium.webdriver.common.by import By

user_table = (By.XPATH, "//table[@table-title]")
search_input = (By.XPATH, "//input[@ng-model='searchValue']")
add_user_button = (By.XPATH, "//button[@type='add']")


def get_user_by_username(text):
    return By.XPATH, "//tbody//tr//td[3][text()='{}']".format(text)


def get_delete_by_username(text):
    return By.XPATH, "//tbody//tr[td[3][text()='{}']]//button[i[contains(@class, 'icon-remove')]]".format(text)
