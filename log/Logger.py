import logging

class Logger():
    def __init__(self, name:str, filename:str=None):
        self.__name = name.upper()
        self.__filename = filename if filename != None else f"{name}.log"
        self.logger = self.__init_logger()
        self.__log_type_dict = {
            logging.DEBUG: lambda message: self.logger.debug(msg= message),
            logging.INFO: lambda message: self.logger.info(msg= message),
            logging.WARNING: lambda message: self.logger.warning(msg= message),
            logging.ERROR: lambda message: self.logger.error(msg= message),
            logging.CRITICAL: lambda message: self.logger.critical(msg= message)
        }

    def __init_logger(self):
        logger = logging.getLogger(name=self.__name)
        logger.setLevel(logging.DEBUG)
        
        ch, fh = logging.StreamHandler(), logging.FileHandler(filename= self.__filename)
        fmt = logging.Formatter(fmt='%(asctime)s [%(name)s][%(levelname)s] - %(message)s',  datefmt="%y-%m-%d %H:%M:%S")
        ch.setFormatter(fmt= fmt)
        fh.setFormatter(fmt= fmt)

        logger.addHandler(ch)
        logger.addHandler(fh)

        return logger

    def log(self, message:str, level:int=logging.DEBUG):
        self.__log_type_dict[level](message = message)


DEBUG = logging.DEBUG
INFO = logging.INFO
WARNING = logging.WARNING
ERROR = logging.ERROR
CRITICAL = logging.CRITICAL