from framework.browser.BrowserFactory import BrowserFactory
from framework.utils.LogUtils import LogUtils


class MetaSingleton(type):

    _instances = {}

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            cls._instances[cls] = super(MetaSingleton, cls).__call__(*args, **kwargs)
        return cls._instances[cls]

    def clear(cls):
        try:
            del MetaSingleton._instances[cls]
        except KeyError:
            LogUtils().make_log('ERROR Class MetaSingleton has no instances to delete')


class Singleton(metaclass=MetaSingleton):

    def __init__(self):
        self.__driver = BrowserFactory().get_webdriver()

    def get_driver(self):
        return self.__driver

    def get_current_url(self):
        LogUtils().make_log('Getting current url')
        return self.__driver.current_url

    def quit_driver(self):
        self.__driver.quit()
