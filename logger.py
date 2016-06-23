"""
    Create a log file to log details

Author : Rohan Nagalkar
"""
import logging


def get_logger(all_log, error_log, append=1):
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)

    handler = logging.StreamHandler()
    handler.setLevel(logging.INFO)
    formatter = logging.Formatter("[%(levelname)s %(asctime)s] %(filename)s: %(lineno)d - %(message)s",
                                  "%Y-%m-%d %H:%M:%S")
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    try:
        if append == 1:
            handler = logging.FileHandler(error_log)
        else:
            handler = logging.FileHandler(error_log, "a")
        handler.setLevel(logging.ERROR)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

        if append == 1:
            handler = logging.FileHandler(all_log)
        else:
            handler = logging.FileHandler(all_log, "a")
        handler.setLevel(logging.DEBUG)
        handler.setFormatter(formatter)
        logger.addHandler(handler)

    except Exception:
        print "Unable to create log file"
        return False

    return logger


def close_logger(log):
    del log
