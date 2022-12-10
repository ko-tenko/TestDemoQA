import json
from pathlib import Path
from framework.utils.LogUtils import LogUtils


class GetUtils:

    @staticmethod
    def get_steps(key: str):
        base_path = Path(__file__).parent
        file_path = (base_path / "../data/steps.json").resolve()
        LogUtils().make_log(f'Getting data for step from {file_path}')
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data[key]

    @staticmethod
    def get_format(key: str):
        base_path = Path(__file__).parent
        file_path = (base_path / "../data/formats.json").resolve()
        LogUtils().make_log(f'Getting data format from {file_path}')
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data[key]

    @staticmethod
    def get_calendar(key: str):
        base_path = Path(__file__).parent
        file_path = (base_path / "../data/calendar.json").resolve()
        LogUtils().make_log(f'Getting data for calendar from {file_path}')
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data[key]

    @staticmethod
    def get_checks(key: str):
        base_path = Path(__file__).parent
        file_path = (base_path / "../data/checks.json").resolve()
        LogUtils().make_log(f'Getting data for checks from {file_path}')
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data[key]

    @staticmethod
    def get_script(key: str):
        base_path = Path(__file__).parent
        file_path = (base_path / "../data/scripts.json").resolve()
        LogUtils().make_log(f'Getting script from {file_path}')
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data[key]

    @staticmethod
    def get_user_data(user_number):
        base_path = Path(__file__).parent
        file_path = (base_path / "../data/user_data.json").resolve()
        LogUtils().make_log(f'Getting user data for registration from {file_path}')
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data[user_number]
