import selenium.webdriver


def before_scenario(context, scenario):
    context.browser = selenium.webdriver.Chrome()
    context.browser.implicitly_wait(15)
    context.browser.get("http://www.way2automation.com/angularjs-protractor/webtables/")


def after_scenario(context, scenario):
    context.browser.quit()
