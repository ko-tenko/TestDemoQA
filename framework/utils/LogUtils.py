import inspect
import logging


class LogUtils:

    @staticmethod
    def make_log(message: str):
        func = inspect.currentframe().f_back.f_code
        logger_name = inspect.stack()[1][3]
        logger = logging.getLogger(logger_name)
        logger.setLevel(logging.DEBUG)
        file_handler = logging.FileHandler('../data/log_file.log', mode="a+")
        formatter_file = logging.Formatter(f'%(asctime)s - {func.co_name} - %(message)s')
        file_handler.setFormatter(formatter_file)
        logger.addHandler(file_handler)
        logger.warning(msg=message)
        logger.removeHandler(file_handler)
