import json
from pathlib import Path
from framework.utils.LogUtils import LogUtils


class ConfigUtils:

    @staticmethod
    def get_config(key: str):
        base_path = Path(__file__).parent
        file_path = (base_path / "../data/config.json").resolve()
        LogUtils().make_log(f'Getting data from {file_path}')
        with open(file_path, "r", encoding="utf-8") as file:
            data = json.load(file)
            return data[key]
