from selenium.webdriver.common.by import By
from framework.elements.Button import Button
from project.pages.BaseForm import BaseForm
from project.utils.GetUtils import GetUtils


class ElementsForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Elements Page"
    page_locator = f"//*[@class='main-header' and contains(text(), '{GetUtils().get_steps('elements')}')]"
    button_web_tables = Button(by_x, "//*[@class='element-group']//*[contains(text(), 'Tables')]", "Web tables menu")
    button_upload_and_download = Button(by_x, "//*[@class='menu-list']//*[contains(text(), 'Upload')]", "Upload and Download")

    def click_web_tables_menu(self):
        self.button_web_tables.click()

    def click_button_upload_and_download(self):
        self.button_upload_and_download.click()
