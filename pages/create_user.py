from selenium.webdriver.common.by import By

first_name_input = (By.XPATH, "//input[@name='FirstName']")
last_name_input = (By.XPATH, "//input[@name='LastName']")
user_name_input = (By.XPATH, "//input[@name='UserName']")
password_input = (By.XPATH, "//input[@name='Password']")
email_input = (By.XPATH, "//input[@name='Email']")
cellphone_input = (By.XPATH, "//input[@name='Mobilephone']")

role_select = (By.XPATH, "//select[@name='RoleId']")

close_button = (By.XPATH, "//button[text()='Close']")
save_button = (By.XPATH, "//button[text()='Save']")


def get_customer_radio_button(text):
    return By.XPATH, "//label[text()='{}' and ./input[@type='radio']]".format(text)
