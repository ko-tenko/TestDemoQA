from selenium.webdriver.common.by import By
from framework.driver.JsUtils import JsUtils
from framework.elements.Button import Button
from framework.elements.TextField import TextField
from project.pages.BaseForm import BaseForm
from project.utils.CreateUtils import CreateUtils
from project.utils.GetUtils import GetUtils


class WebTablesForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Web Tables Page"
    page_locator = "//*[@class='main-header' and contains(text(), 'Web Tables')]"
    footer_remove = GetUtils().get_script('footer_remove')
    iframe_remove = GetUtils().get_script('iframe_remove')
    button_add = Button(by_x, "//*[@id='addNewRecordButton']", "Add")
    first_name = TextField(by_x, "//*[@id='firstName']", "field First Name")
    last_name = TextField(by_x, "//*[@id='lastName']", "field Last Name")
    email = TextField(by_x, "//*[@id='userEmail']", "field Email")
    age = TextField(by_x, "//*[@id='age']", "field Age")
    salary = TextField(by_x, "//*[@id='salary']", "field Salary")
    department = TextField(by_x, "//*[@id='department']", "field Department")
    button_submit = Button(by_x, "//button[@id='submit']", "Submit")
    table_text = TextField(by_x, "//*[@class='rt-tbody']", "Table text")
    button_delete = Button(by_x, "//*[@class='action-buttons']//*[@title='Delete']", "Delete buttons")
    button_delete_record = Button(by_x, "//*[@id='delete-record-4']", "Delete record")

    def click_button_add(self):
        self.button_add.click()

    def send_data_to_registration_form(self, user_dict):
        user = CreateUtils().create_user(user_dict)
        self.first_name.send_text(user.first_name)
        self.last_name.send_text(user.last_name)
        self.email.send_text(user.email)
        self.age.send_text(user.age)
        self.salary.send_text(user.salary)
        self.department.send_text(user.department)

    def click_submit_button(self):
        self.button_submit.click()

    def get_table_text(self):
        return self.table_text.get_text()

    def click_button_delete_record(self):
        self.button_delete_record.click()

    def count_rows_in_table(self):
        return len(self.button_delete.find_the_elements())

    def remove_footer(self):
        JsUtils().remove_content(self.footer_remove)

    def remove_iframe(self):
        JsUtils().remove_content(self.iframe_remove)
