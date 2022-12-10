import os
import time
from datetime import datetime
from framework.utils.ConfigUtils import ConfigUtils
from framework.utils.LogUtils import LogUtils
from project.utils.GetUtils import GetUtils


class SysUtils:

    @staticmethod
    def clear_folder():
        temp_path = os.path.abspath('../temp')
        LogUtils().make_log(f'Clearing folder {temp_path}')
        for file in os.scandir(temp_path):
            file_path = os.path.join(temp_path, file.name)
            os.remove(file_path)

    @staticmethod
    def get_files_number():
        dir_path = os.path.abspath('../temp')
        LogUtils().make_log(f'Getting files number in directory {dir_path}')
        files_list = [file for file in os.scandir(dir_path)]
        files_number = len(files_list)
        return files_number

    @staticmethod
    def is_download_started(files_before_dl):
        LogUtils().make_log(f'Check if the file download has started')
        start_time = datetime.now()
        while files_before_dl == SysUtils().get_files_number():
            current_time = datetime.now()
            if (current_time - start_time).seconds > ConfigUtils().get_config('timeout_dl'):
                return False
            continue
        return True

    @staticmethod
    def is_file_downloaded():
        LogUtils().make_log(f'Checking that the file is downloaded')
        start_time = datetime.now()
        while SysUtils().get_last_added_file().endswith('tmp') or \
                SysUtils().get_last_added_file().endswith('download'):
            current_time = datetime.now()
            if (current_time - start_time).seconds > ConfigUtils().get_config('timeout_dl'):
                return False
            continue
        return True

    @staticmethod
    def get_last_added_file():
        dir_path = os.path.abspath('../temp')
        LogUtils().make_log(f'Getting the last added file')
        files_dict = {}
        for file in os.scandir(dir_path):
            file_creation_time = time.strftime(GetUtils().get_format('file_info'), time.gmtime(os.path.getmtime(file.path)))
            file_name = file.name
            file_path = file.path
            files_dict[file_name] = [file_creation_time, file_path]
        dict_sorted = dict(sorted(files_dict.items(), key=lambda value: value[0], reverse=True))
        path_of_last_added_file = dict_sorted[list(dict_sorted.keys())[0]]
        file_path = path_of_last_added_file[1].replace('\\', '/')
        return file_path

    @staticmethod
    def get_downloaded_file_name():
        dir_path = os.path.abspath('../temp')
        LogUtils().make_log(f"Getting the file's name")
        files_dict = {}
        for file in os.scandir(dir_path):
            file_creation_time = time.strftime(GetUtils().get_format('file_info'), time.gmtime(os.path.getmtime(file.path)))
            file_name = file.name
            files_dict[file_name] = [file_creation_time]
        dict_sorted = dict(sorted(files_dict.items(), key=lambda value: value, reverse=True))
        file_name = list(dict_sorted.keys())[0]
        return file_name
