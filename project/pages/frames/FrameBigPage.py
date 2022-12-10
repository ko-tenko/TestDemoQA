from selenium.webdriver.common.by import By
from framework.elements.TextField import TextField
from project.pages.BaseForm import BaseForm


class FrameBigForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Big Frame Page"
    page_locator = "//*[@id='sampleHeading']"
    frame_big_txt = TextField(by_x, "//*[@id='sampleHeading']", "Big frame")

    def get_big_text(self):
        return self.frame_big_txt.receive_text()
