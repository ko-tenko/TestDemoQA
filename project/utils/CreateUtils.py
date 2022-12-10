from framework.utils.LogUtils import LogUtils
from project.pages.forms.Calendar import Calendar
from project.pages.forms.User import User
from project.utils.GetUtils import GetUtils


class CreateUtils:

    @staticmethod
    def create_user(user_dict):
        LogUtils().make_log('Creating user profile for registration')
        return User(
            first_name=user_dict['first_name'],
            last_name=user_dict['last_name'],
            email=user_dict['email'],
            age=user_dict['age'],
            salary=user_dict['salary'],
            department=user_dict['department']
        )

    @staticmethod
    def create_calendar():
        LogUtils().make_log('Creating calendar')
        return Calendar(
            day=GetUtils().get_calendar('day'),
            month=GetUtils().get_calendar('month'),
            month_num=GetUtils().get_calendar('month_num')
        )
