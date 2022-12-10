from selenium.webdriver.common.by import By
from framework.elements.Button import Button
from project.pages.BaseForm import BaseForm


class LinksForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Links Page"
    page_locator = "//*[@id='linkWrapper']"
    button_home = Button(by_x, "//*[@id='simpleLink']", "Home page")

    def click_button_home(self):
        self.button_home.click()
