from selenium.webdriver.common.by import By
from framework.driver.IFrameUtils import IFrameUtils
from framework.elements.Button import Button
from project.pages.BaseForm import BaseForm
from project.utils.GetUtils import GetUtils


class NestedForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Nested Page"
    page_locator = f"//*[@class='main-header' and contains(text(), '{GetUtils().get_steps('header_nested')}')]"
    button_frames = Button(by_x, f"//*[@class='text' and text()='{GetUtils().get_steps('frames')}']", "Frames")
    frame_parent_locator = "//iframe[@id='frame1']"

    def switch_to_iframe(self):
        IFrameUtils().switch_to_iframe(self.by_x, self.frame_parent_locator)

    def click_button_frames(self):
        self.button_frames.click()
