from framework.browser.Singleton import Singleton
from framework.utils.LogUtils import LogUtils


class Handles:

    @staticmethod
    def handle_current_window():
        LogUtils().make_log('Handling current window')
        return Singleton().get_driver().current_window_handle

    @staticmethod
    def get_window_handles():
        LogUtils().make_log('Getting handles for window')
        return Singleton().get_driver().window_handles

    @staticmethod
    def switch_to_new_window():
        LogUtils().make_log('Switching to new window')
        windows_list = Handles.get_window_handles()
        Singleton().get_driver().switch_to.window(windows_list[-1])

    @staticmethod
    def remove_window_from_list(window_name):
        LogUtils().make_log('Removing window from list')
        windows_list = Handles.get_window_handles()
        Singleton().get_driver().switch_to.window(windows_list.remove(window_name))

    @staticmethod
    def switch_to_original(window_name):
        LogUtils().make_log('Switching to original window window')
        Singleton().get_driver().switch_to.window(window_name)

    @staticmethod
    def close_tab():
        LogUtils().make_log('Closing tab')
        Singleton().get_driver().close()
