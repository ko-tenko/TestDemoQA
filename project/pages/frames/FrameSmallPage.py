from selenium.webdriver.common.by import By
from framework.elements.TextField import TextField
from project.pages.BaseForm import BaseForm


class FrameSmallForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Small Frame Page"
    page_locator = "//*[@id='sampleHeading']"
    frame_small_txt = TextField(by_x, "//*[@id='sampleHeading']", "Frame Child")

    def get_small_text(self):
        return self.frame_small_txt.receive_text()
