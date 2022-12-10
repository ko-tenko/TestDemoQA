from framework.driver.Waits import Waits
from framework.utils.LogUtils import LogUtils


class Alerts:

    @staticmethod
    def alert_is_present():
        LogUtils().make_log('Checking for Alert presence')
        return Waits.wait_alert_is_present()

    @staticmethod
    def alert_text():
        LogUtils().make_log('Getting text from Alert')
        alert = Alerts().alert_is_present()
        return alert.text

    @staticmethod
    def accept_alert():
        LogUtils().make_log('Accepting Alert')
        alert = Alerts().alert_is_present()
        alert.accept()

    @staticmethod
    def send_data(some_data):
        LogUtils().make_log('Sending data Alert')
        alert = Alerts().alert_is_present()
        alert.send_keys(some_data)

    @staticmethod
    def alert_is_not_present():
        LogUtils().make_log('Checking that Alert is not present')
        return Waits.wait_alert_is_not_present()

    @staticmethod
    def dismiss_alert():
        LogUtils().make_log('Dismissing Alert')
        alert = Alerts().alert_is_present()
        alert.dismiss()
