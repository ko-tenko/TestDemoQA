import pytest
from framework.browser.Singleton import Singleton
from framework.utils.ConfigUtils import ConfigUtils
from framework.utils.LogUtils import LogUtils
from project.utils.SysUtils import SysUtils


@pytest.fixture()
def driver():
    LogUtils().make_log("Creating the driver's object")
    yield Singleton().get_driver()
    LogUtils().make_log("Quitting the driver's object")
    Singleton().quit_driver()
    Singleton.clear()


@pytest.fixture()
@pytest.mark.usefixtures('driver')
def open_page(driver):
    LogUtils().make_log("Opening start url")
    driver.get(ConfigUtils().get_config('url'))


@pytest.fixture()
def clear_folder():
    LogUtils().make_log("Clearing folder temp")
    SysUtils().clear_folder()
