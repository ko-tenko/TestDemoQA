from selenium.webdriver.common.by import By
from framework.elements.Button import Button
from framework.elements.TextField import TextField
from project.pages.BaseForm import BaseForm
from project.utils.SysUtils import SysUtils
from project.utils.GetUtils import GetUtils


class UpDownLoadForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Upload and Download Page"
    page_locator = f"//*[@class='main-header' and contains(text(), '{GetUtils().get_steps('file')}')]"
    button_download = Button(by_x, "//*[@id='downloadButton']", "Download")
    input_for_upload = TextField(by_x, "//input[@id='uploadFile']", "Upload")
    uploaded_file_path = TextField(by_x, "//*[@id='uploadedFilePath']", "Uploaded file path")

    def click_button_download(self):
        self.button_download.click()

    def upload_file_to_webpage(self):
        file_path = SysUtils().get_last_added_file()
        self.input_for_upload.send_text(file_path)

    def get_uploaded_file_path(self):
        return self.uploaded_file_path.receive_text()
