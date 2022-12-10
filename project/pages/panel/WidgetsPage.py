from selenium.webdriver.common.by import By
from framework.elements.Button import Button
from project.pages.BaseForm import BaseForm
from project.utils.GetUtils import GetUtils


class WidgetsForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Widgets Page"
    page_locator = f"//*[@class='main-header' and contains(text(), '{GetUtils().get_steps('widgets')}')]"
    button_date_picker = Button(by_x, f"//*[contains(text(), '{GetUtils().get_steps('picker')}')]", "Date Picker")

    def click_button_date_picker(self):
        self.button_date_picker.click()
