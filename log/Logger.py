import logging

class Logger():
    def __init__(self, name:str, filename:str=None):
        self.__name = name.upper()
        self.__filename = filename
        self.logger = self.__init_logger()
        self.__log_type_dict = {
            logging.DEBUG: lambda message: self.logger.debug(msg= message),
            logging.INFO: lambda message: self.logger.info(msg= message),
            logging.WARNING: lambda message: self.logger.warning(msg= message),
            logging.ERROR: lambda message: self.logger.error(msg= message),
            logging.CRITICAL: lambda message: self.logger.critical(msg= message)
        }

    def __init_streamHandler(self, fmt:logging.Formatter):
        ch = logging.StreamHandler()
        ch.setFormatter(fmt= fmt)
        return ch

    def __init_fileHandler(self, fmt:logging.Formatter):
        fh = logging.FileHandler(self.__filename)
        fh.setFormatter(fmt= fmt)
        return fh

    def __init_logger(self):
        logger = logging.getLogger(name=self.__name)
        logger.setLevel(logging.DEBUG)

        fmt = logging.Formatter(fmt='%(asctime)s [%(name)s][%(levelname)s] - %(message)s',  datefmt="%y-%m-%d %H:%M:%S")

        ch = self.__init_streamHandler(fmt=fmt)
        logger.addHandler(ch)

        if self.__filename is not None:
            fh = self.__init_fileHandler(fmt=fmt)
            logger.addHandler(fh)

        return logger

    def log(self, message:str, level:int=logging.DEBUG):
        self.__log_type_dict[level](message = message)


DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL