from selenium.webdriver.common.by import By
from framework.elements.TextField import TextField
from project.pages.BaseForm import BaseForm


class FrameChildForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Child Frame Page"
    page_locator = "//*[contains(text(), 'Child Iframe')]"
    frame_child_txt = TextField(by_x, "//body", "Small frame")

    def get_iframe_child_text(self):
        return self.frame_child_txt.receive_text()
