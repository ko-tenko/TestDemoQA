from selenium.webdriver import ActionChains
from framework.browser.Singleton import Singleton
from framework.driver.Waits import Waits
from framework.utils.LogUtils import LogUtils
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException


class BaseElement:

    def __init__(self, by_x, locator, name):
        self.by_x = by_x
        self.locator = locator
        self.name = name

    def click(self):
        element = None
        LogUtils().make_log(f'Clicking on the {self.name}')
        try:
            element = Waits.wait_until_element_clickable((self.by_x, self.locator)).click()
        except ElementClickInterceptedException:
            LogUtils().make_log(f'ERROR element {self.name} is not clickable')
        return element

    def find_the_element(self):
        element = None
        LogUtils().make_log(f'Find element {self.name}')
        try:
            element = Singleton().get_driver().find_element(self.by_x, self.locator)
        except NoSuchElementException:
            LogUtils().make_log(f'ERROR element {self.name} not found')
        return element

    def find_the_elements(self):
        LogUtils().make_log(f'Find elements {self.name}')
        return Singleton().get_driver().find_elements(self.by_x, self.locator)

    def get_text(self):
        LogUtils().make_log(f'Getting text from {self.name}')
        return Waits.wait_until_visibility((self.by_x, self.locator)).text

    def get_attribute_text(self, attribute):
        LogUtils().make_log(f'Getting text from attribute {self.name}')
        element = Waits.wait_until_visibility((self.by_x, self.locator))
        attribute_text = element.get_attribute(attribute)
        return attribute_text

    def hover(self):
        LogUtils().make_log(f'Hovering on {self.name}')
        element = Singleton().get_driver().find_element(self.by_x, self.locator)
        ActionChains(Singleton().get_driver()).move_to_element(element).perform()

    def send_key(self, txt):
        LogUtils().make_log(f'Sending data to {self.name}')
        Waits.wait_until_visibility((self.by_x, self.locator)).send_keys(txt)
