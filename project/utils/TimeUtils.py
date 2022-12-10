from framework.utils.LogUtils import LogUtils
from project.utils.CreateUtils import CreateUtils
from project.utils.GetUtils import GetUtils
from datetime import datetime, date
from calendar import monthrange


class TimeUtils:

    @staticmethod
    def get_nearest_year():
        LogUtils().make_log(f'calculating the closest year to February 29')
        new_calendar = CreateUtils().create_calendar()
        current_year = datetime.now().year
        now = datetime.now()
        years_dict = {}
        for year in range(current_year - 2, current_year + 3):
            month_number = int(new_calendar.month_num)
            days_in_month = monthrange(year, month_number)[1]
            if days_in_month == 29:
                leap_date = date(year, month_number, int(new_calendar.day))
                difference = (date(now.year, now.month, now.day) - leap_date).days
                leap_year = leap_date.year
                years_dict[difference] = leap_year
        nearest_year = years_dict[min(years_dict)]
        return nearest_year

    @staticmethod
    def get_difference():
        LogUtils().make_log(f'calculating difference between two dates')
        new_calendar = CreateUtils().create_calendar()
        year = TimeUtils().get_nearest_year()
        now = datetime.now()
        month_number = int(new_calendar.month_num)
        leap_date = date(year, month_number, 29)
        difference = (date(now.year, now.month, now.day) - leap_date).days
        return difference

    @staticmethod
    def get_desired_month_and_year():
        LogUtils().make_log(f'Getting month and year')
        new_calendar = CreateUtils().create_calendar()
        return " ".join([new_calendar.month, str(TimeUtils().get_nearest_year())])

    @staticmethod
    def get_desired_date():
        LogUtils().make_log(f'Getting date')
        new_calendar = CreateUtils().create_calendar()
        day = new_calendar.day
        month = new_calendar.month_num
        year = TimeUtils().get_nearest_year()
        desired_date = f"0{month}/{day}/{year}"
        return desired_date

    @staticmethod
    def get_current_date_and_time():
        LogUtils().make_log(f'Getting current date and time')
        date_format = GetUtils().get_format('format_date_time')
        date_and_time = datetime.now().strftime(date_format)
        return date_and_time

    @staticmethod
    def get_current_date():
        LogUtils().make_log(f'Getting current date')
        date_format = GetUtils().get_format('format_date')
        date_now = datetime.now().strftime(date_format)
        return date_now
