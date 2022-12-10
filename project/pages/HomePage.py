from selenium.webdriver.common.by import By
from framework.elements.Button import Button
from project.pages.BaseForm import BaseForm
from project.utils.GetUtils import GetUtils


class HomeForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Home Page"
    page_locator = "//img[@class='banner-image']"
    button_alert = Button(by_x, f"//*[contains(text(), '{GetUtils().get_steps('alert_menu')}')]", "Alert menu")
    button_elements = Button(by_x, f"//*[@id='app']//*[contains(text(), '{GetUtils().get_steps('elements')}')]", "Elements menu")
    button_widgets = Button(by_x, f"//*[@id='app']//*[contains(text(), '{GetUtils().get_steps('widgets')}')]", "Widgets menu")

    def click_alerts_menu(self):
        self.button_alert.click()

    def click_elements_menu(self):
        self.button_elements.click()

    def click_widgets_menu(self):
        self.button_widgets.click()
