from selenium.webdriver.common.by import By
from framework.elements.Button import Button
from project.pages.BaseForm import BaseForm


class BrowserWindowsForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_locator = "//*[@class='main-header' and contains(text(), 'Browser Windows')]"
    page_name = "Browser Windows Page"
    button_new_tab = Button(by_x, "//*[@id='tabButton']", "New tab")
    button_links_submenu = Button(by_x, "//*[@id='item-5']//*[contains(text(), 'Links')]", "Links submenu")
    button_elements_menu = Button(by_x, "//*[@class='group-header']//*[contains(text(), 'Elements')]", "Elements menu")

    def click_button_new_tab(self):
        self.button_new_tab.click()

    def click_button_elements_menu(self):
        self.button_elements_menu.click()

    def click_button_links_submenu(self):
        self.button_links_submenu.click()
