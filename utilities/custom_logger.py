import logging
import inspect

class LogGen:

    def loggen(loglevel=logging.DEBUG):
        # Gets the name of the class / method from where this method is called
        loggerName = inspect.stack()[1][3]
        logger = logging.getLogger(loggerName)
        # By default, log all messages
        logger.setLevel(logging.DEBUG)

        # By default, log all messages
        fileHandler = logging.FileHandler("automation.log", mode='a')
        fileHandler.setLevel(loglevel)

        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s: %(message)s',
                                      datefmt='%m/%d/%Y %I:%M:%S %p')

        #adds formater to handler
        fileHandler.setFormatter(formatter)

        #adds handler to logger
        logger.addHandler(fileHandler)

        return logger
