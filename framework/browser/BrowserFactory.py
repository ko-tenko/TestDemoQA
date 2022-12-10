import os
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
from framework.utils.ConfigUtils import ConfigUtils


class BrowserFactory:

    __file_path = os.path.abspath(ConfigUtils().get_config('path'))
    __prefs = {ConfigUtils().get_config('dl_directory'): __file_path}

    @staticmethod
    def get_webdriver():
        browser_name = ConfigUtils().get_config("browser")
        if browser_name == "chrome":
            return BrowserFactory().__chrome_driver()
        elif browser_name == "firefox":
            return BrowserFactory().__firefox_driver()

    @staticmethod
    def __chrome_driver():
        chrome_options = webdriver.ChromeOptions()
        for option in ConfigUtils().get_config("options"):
            chrome_options.add_argument(option)
        chrome_options.add_experimental_option("prefs", BrowserFactory.__prefs)
        chrome_service = ChromeService(ChromeDriverManager().install())
        return webdriver.Chrome(service=chrome_service, options=chrome_options)

    @staticmethod
    def __firefox_driver():
        firefox_options = webdriver.FirefoxOptions()
        for option in ConfigUtils().get_config("options"):
            firefox_options.add_argument(option)
        profile = webdriver.FirefoxProfile()
        profile.set_preference('browser.download.dir', BrowserFactory.__file_path)
        firefox_service = FirefoxService(GeckoDriverManager().install())
        return webdriver.Firefox(service=firefox_service, options=firefox_options)
