import logging

logging.basicConfig(level=logging.INFO)


class Logger:
    @staticmethod
    def info(message=None, json=None):
        logging.info(Logger.__log_format(message, json))

    @staticmethod
    def error(message=None, json=None):
        logging.error(Logger.__log_format(message, json))

    @staticmethod
    def warning(message=None, json=None):
        logging.warning(Logger.__log_format(message, json))

    @staticmethod
    def debug(message=None, json=None):
        logging.debug(Logger.__log_format(message, json))

    @staticmethod
    def __log_format(message, json=None):
        return f"{message if message else ''} {json if json else ''}"
