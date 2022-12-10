from selenium.webdriver.common.by import By
from project.pages.BaseForm import BaseForm


class SampleForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Sample Page"
    page_locator = "//*[@id='sampleHeading' and contains(text(), 'sample page')]"
