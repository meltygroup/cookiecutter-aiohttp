# -*- coding: utf-8 -*-

"""
    Utils module who permits to create well formatted loggers.
"""

import sys
import logging


def get_logger(name: str, level=logging.DEBUG) -> logging.Logger:
    """
        Return an instance of logging.Logger configured
        to pretty-print a message.

        :param name: Name of the logger
        :type name: str
        :param level: Level of the logger
        :type level: int
        :return: Instance of logging.Logger
        :rtype: logging.Logger
    """

    logger = logging.getLogger(name)
    logger_stream = logging.StreamHandler(sys.stdout)
    stream_formatter = logging.Formatter(
        "[%(asctime)s] [%(levelname)s] [%(name)s]: %(message)s"
    )

    logger.setLevel(level)
    logger_stream.setLevel(level)
    logger_stream.setFormatter(stream_formatter)
    logger.addHandler(logger_stream)
    return logger
