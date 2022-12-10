from framework.browser.Singleton import Singleton
from framework.utils.LogUtils import LogUtils


class JsUtils:

    @staticmethod
    def remove_content(script_js):
        LogUtils().make_log('Removing ads from the page')
        Singleton().get_driver().execute_script(script_js)

    @staticmethod
    def scroll_to_the_bottom(script_js):
        LogUtils().make_log('Scrolling to the element')
        Singleton().get_driver().execute_script(script_js)
