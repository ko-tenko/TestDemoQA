from framework.elements.BaseElement import BaseElement
from framework.utils.LogUtils import LogUtils


class BaseForm:

    def __init__(self, by_x, page_locator, page_name):
        self.by_x = by_x
        self.page_locator = page_locator
        self.page_name = page_name

    def is_page_opened(self):
        LogUtils().make_log(f'Opening the {self.page_name}')
        element = BaseElement(self.by_x, self.page_locator, self.page_name).find_the_elements()
        if len(element) == 0:
            (LogUtils().make_log(f'ERROR {self.page_name} is not opened'))
            return False
        (LogUtils().make_log(f'{self.page_name} page is opened'))
        return True
