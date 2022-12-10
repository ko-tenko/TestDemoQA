from selenium.webdriver.common.by import By
from framework.elements.Button import Button
from framework.elements.TextField import TextField
from project.pages.BaseForm import BaseForm
from project.utils.TimeUtils import TimeUtils
from project.utils.GetUtils import GetUtils


class DatePickerForm(BaseForm):

    def __init__(self):
        super().__init__(self.by_x, self.page_locator, self.page_name)

    by_x = By.XPATH
    page_name = "Date Picker Page"
    page_locator = f"//*[@class='main-header' and contains(text(), '{GetUtils().get_steps('picker')}')]"
    field_select_date = TextField(by_x, "//*[@id='datePickerMonthYearInput']", "Select Date")
    field_date_and_time = TextField(by_x, "//*[@id='dateAndTimePickerInput']", "Date and Time")
    header_month_year = TextField(by_x, "//*[contains(@class, 'current')]", "Month Year")
    attribute = GetUtils.get_steps('attribute')
    button_next_month = Button(by_x, "//*[contains(text(), 'Next Month')]", "Next Month")
    button_previous_month = Button(by_x, "//*[contains(text(), 'Previous Month')]", "Next Month")
    button_29_february = Button(by_x, f"//*[contains(text(), '{GetUtils.get_steps('day')}') and"
                              f" contains(@aria-label, '{GetUtils.get_steps('month')}')]", "29 February")

    def click_on_field_select_date(self):
        self.field_select_date.click()

    def get_data_from_field_select_date(self):
        return self.field_select_date.get_attribute_text(self.attribute)

    def get_data_from_field_date_and_time(self):
        return self.field_date_and_time.get_attribute_text(self.attribute)

    def get_from_header_month_and_year(self):
        return self.header_month_year.receive_text()

    def click_button_next_month(self):
        self.button_next_month.click()

    def click_button_previous_month(self):
        self.button_previous_month.click()

    def select_nearest_month_and_year(self):
        if TimeUtils.get_difference() < 0:
            while self.get_from_header_month_and_year() != TimeUtils.get_desired_month_and_year():
                self.click_button_next_month()
        elif TimeUtils.get_difference() > 0:
            while self.get_from_header_month_and_year() != TimeUtils.get_desired_month_and_year():
                self.click_button_previous_month()
        else:
            return True

    def select_29_february(self):
        self.button_29_february.click()
