# -*- coding: utf-8 -*-

"""
    Tests for the `/logger.py` module.
"""

import logging
import logger as logger


def test_basic_logger(capfd):
    """
        Test the output of a basic logger (any level).
    """
    logging.raiseExceptions = False
    log = logger.get_logger("my_test")
    log.debug("hello world!")
    out, err = capfd.readouterr()
    assert "hello world!" in out
    assert err == ""


def test_higher_level_logger(capfd):
    """
        Test the output of a logger configured to output
        a message with a level >= INFO.
    """
    logging.raiseExceptions = False
    log = logger.get_logger("my_test", level=logging.INFO)
    log.debug("hello world!")
    out, err = capfd.readouterr()
    assert out == ""
    assert err == ""
