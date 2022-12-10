from selenium.webdriver.common.by import By
from framework.driver.IFrameUtils import IFrameUtils
from project.pages.BaseForm import BaseForm
from project.utils.GetUtils import GetUtils


class FramesForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Frames Page"
    page_locator = f"//*[@class='main-header' and contains(text(), '{GetUtils().get_steps('header_frames')}')]"
    frame_big_locator = "//iframe[@id='frame1']"
    frame_small_locator = "//iframe[@id='frame2']"

    def switch_to_big_iframe(self):
        IFrameUtils().switch_to_iframe(self.by_x, self.frame_big_locator)

    def switch_to_small_iframe(self):
        IFrameUtils().switch_to_iframe(self.by_x, self.frame_small_locator)
