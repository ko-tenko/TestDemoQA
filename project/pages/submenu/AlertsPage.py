from selenium.webdriver.common.by import By
from framework.driver.JsUtils import JsUtils
from framework.elements.Button import Button
from framework.elements.TextField import TextField
from project.pages.BaseForm import BaseForm
from project.utils.GetUtils import GetUtils


class AlertsForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Alerts Page"
    page_locator = f"//*[@class='main-header' and contains(text(), '{GetUtils().get_steps('header_alerts')}')]"
    button_alerts_menu = Button(by_x, f"//*[@class='text' and text()='{GetUtils().get_steps('alerts')}']", "Alerts menu")
    button_nested_frames = Button(by_x, f"//*[@class='text' and text()='{GetUtils().get_steps('nested')}']", "Nested frames")
    footer_remove = GetUtils().get_script('footer_remove')
    iframe_remove = GetUtils().get_script('iframe_remove')
    button_alert = Button(by_x, "//*[@id='alertButton']", "Alert")
    button_confirm_box = Button(by_x, "//*[@id='confirmButton']", "Confirm box")
    button_browser_windows = Button(by_x, "//*[@id='item-0']//*[contains(text(), 'Browser Windows')]", "Browser windows")
    confirm_box_text = TextField(by_x, "//*[@id='confirmResult']", "Confirm box Text")
    ads_button = Button(by_x, "//*[@id='fixedban']", "Advertising")
    button_prompt = Button(by_x, "//*[@id='promtButton']", "Prompt")
    prompt_text = TextField(by_x, "//*[@id='promptResult']", "Prompt")

    def click_button_alerts_menu(self):
        self.button_alerts_menu.click()

    def click_button_alert(self):
        self.button_alert.click()

    def click_button_nested_frames(self):
        self.button_nested_frames.click()

    def click_button_confirm_box(self):
        self.button_confirm_box.click()

    def text_in_confirm_box(self):
        return self.confirm_box_text.receive_text()

    def click_button_prompt(self):
        self.button_prompt.click()

    def text_in_prompt(self) -> str:
        random_text = self.prompt_text.receive_text().split()
        return random_text[2]

    def click_button_browser_windows(self):
        self.button_browser_windows.click()

    def remove_footer(self):
        JsUtils().remove_content(self.footer_remove)

    def remove_iframe(self):
        JsUtils().remove_content(self.iframe_remove)
