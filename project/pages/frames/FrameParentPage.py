from selenium.webdriver.common.by import By
from framework.driver.IFrameUtils import IFrameUtils
from framework.elements.TextField import TextField
from project.pages.BaseForm import BaseForm


class FrameParentForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Parent Frame Page"
    page_locator = "//*[contains(text(), 'Parent')]"
    frame_parent_txt = TextField(by_x, "//body", "Frame parent")
    frame_child_locator = "//iframe"

    def get_iframe_parent_text(self):
        return self.frame_parent_txt.receive_text()

    def switch_to_iframe(self):
        IFrameUtils().switch_to_iframe(self.by_x, self.frame_child_locator)
