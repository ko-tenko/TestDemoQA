from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as EC
from framework.browser.Singleton import Singleton
from framework.utils.ConfigUtils import ConfigUtils
from selenium.common.exceptions import TimeoutException, ElementNotVisibleException, \
    ElementClickInterceptedException, NoSuchElementException
from framework.utils.LogUtils import LogUtils


class Waits:

    @staticmethod
    def wait_until_visibility(locator):
        element = None
        wait = Wait(Singleton().get_driver(), ConfigUtils().get_config('timeout'))
        try:
            element = wait.until(EC.visibility_of_element_located(locator))
        except ElementNotVisibleException:
            LogUtils().make_log('ERROR Element is not visible')
        return element

    @staticmethod
    def wait_until_element_clickable(locator):
        element = None
        wait = Wait(Singleton().get_driver(), ConfigUtils().get_config('timeout'))
        try:
            element = wait.until(EC.element_to_be_clickable(locator))
        except ElementClickInterceptedException:
            LogUtils().make_log(f'ERROR click intercepted')
        return element

    @staticmethod
    def wait_alert_is_present():
        element = None
        wait = Wait(Singleton().get_driver(), ConfigUtils().get_config('timeout'))
        try:
            element = wait.until(EC.alert_is_present())
        except TimeoutException:
            LogUtils().make_log(f'ERROR Alert is not present')
        return element

    @staticmethod
    def wait_alert_is_not_present():
        wait = Wait(Singleton().get_driver(), ConfigUtils().get_config('timeout_alert'))
        try:
            wait.until(EC.alert_is_present())
        except TimeoutException:
            LogUtils().make_log(f'Alert closed correctly')
            return True

    @staticmethod
    def is_element_present(locator):
        element = None
        wait = Wait(Singleton().get_driver(), ConfigUtils().get_config('timeout'))
        try:
            element = wait.until(EC.presence_of_element_located(locator))
        except NoSuchElementException:
            LogUtils().make_log(f'ERROR click intercepted')
        return element

    @staticmethod
    def are_elements_present(locator):
        wait = Wait(Singleton().get_driver(), ConfigUtils().get_config('timeout'))
        return wait.until(EC.presence_of_all_elements_located(locator))
