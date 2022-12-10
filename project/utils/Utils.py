import random
import string
from framework.utils.LogUtils import LogUtils


class Utils:

    @staticmethod
    def user_data_in_table(user_dict, table_content):
        LogUtils().make_log(f'Verification of successful registration')
        for value in user_dict.values():
            if value not in table_content:
                return False
            return True

    @staticmethod
    def get_txt_date_and_time(date_string):
        LogUtils().make_log(f'Getting text from field')
        value_list = [value.strip(',') for value in date_string.split()][0:3]
        return value_list

    @staticmethod
    def generate_text() -> str:
        LogUtils().make_log(f'Generating random text')
        letters = string.ascii_letters
        return ''.join(random.choice(letters) for _ in range(10))
