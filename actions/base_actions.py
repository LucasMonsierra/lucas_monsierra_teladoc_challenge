from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


class BaseActions:
    def __init__(self, context):
        self.browser = context.browser

    def click(self, by_locator):
        try:
            WebDriverWait(self.browser, timeout=10).until(
                EC.visibility_of_element_located(by_locator))
            element = self.browser.find_element(*by_locator)
            element.click()
        except:
            assert False, "Exception! Can't click on the element"

    def select(self, by_locator, text):
        try:
            WebDriverWait(self.browser, timeout=10).until(
                EC.visibility_of_element_located(by_locator))
            element = Select(self.browser.find_element(*by_locator))
            element.select_by_visible_text(text)
        except:
            assert False, "Exception! Can't select option {}".format(text)

    def send_text(self, by_locator, keyword):
        try:
            WebDriverWait(self.browser, timeout=10).until(
                EC.visibility_of_element_located(by_locator))
            element = self.browser.find_element(*by_locator)
            element.send_keys(keyword)
        except:
            assert False, "Exception! Can't find on the element"

    def is_displayed(self, by_locator):
        try:
            self.browser.find_element(*by_locator)
            WebDriverWait(self.browser, timeout=10).until(
                EC.visibility_of_element_located(by_locator))
        except:
            assert False, "Exception! Element not displayed"
        assert True, "Test pass"

    def is_invisible(self, by_locator):
        try:
            WebDriverWait(self.browser, timeout=10).until(
                EC.invisibility_of_element_located(by_locator))
        except:
            assert False, "Exception! Element still displayed"
        assert True, "Test pass"

    def is_enabled(self, by_locator):
        try:
            self.browser.find_element(*by_locator)
            WebDriverWait(self.browser, timeout=10).until(
                EC.element_to_be_clickable(by_locator))
        except:
            assert False, "Exception! Element not enabled"
        assert True, "Test pass"
