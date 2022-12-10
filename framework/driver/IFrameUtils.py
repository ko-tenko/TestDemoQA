from framework.browser.Singleton import Singleton
from framework.utils.LogUtils import LogUtils


class IFrameUtils:

    @staticmethod
    def switch_to_iframe(by_x, locator):
        LogUtils().make_log('Switching to iframe')
        iframe = Singleton().get_driver().find_element(by_x, locator)
        Singleton().get_driver().switch_to.frame(iframe)

    @staticmethod
    def switch_to_default_iframe():
        LogUtils().make_log('Switching to default iframe')
        Singleton().get_driver().switch_to.default_content()

    @staticmethod
    def get_current_url():
        return Singleton().get_driver().current_url
