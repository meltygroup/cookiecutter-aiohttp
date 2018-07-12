# -*- coding: utf-8 -*-

"""
    Tests for the `/{{ cookiecutter.project_slug }}.py` module.
"""

from unittest.mock import patch
import sys
import os

import {{ cookiecutter.project_slug }} as app


def test_parse_args():
    """
        Test the argument parser.
    """
    with patch.object(sys, "argv", ['__init__.py']):
        args = app.parse_args()
        assert args.config is None


def test_parse_args_with_config():
    """
        Test the argument parser with a config file.
    """
    args = app.parse_args(["-c", "super_config.toml"])
    assert args.config == "super_config.toml"


def test_locate_config_file():
    """
        Test the priority of the paths when locating the
        configuration file.
    """
    config_path = app.locate_config_file("my_test_app")
    assert config_path is None
    os.mknod("my_test_app.toml")
    os.mkdir("TMP")
    os.mknod("TMP/my_test_app.toml")
    config_path = app.locate_config_file("my_test_app", locations=["./", "TMP/"])
    assert config_path == "./my_test_app.toml"
    os.remove("my_test_app.toml")
    config_path = app.locate_config_file("my_test_app", locations=["./", "TMP/"])
    assert config_path == "TMP/my_test_app.toml"
    os.remove("TMP/my_test_app.toml")
    os.rmdir("TMP")
    config_path = app.locate_config_file("my_test_app", locations=["./", "TMP/"])
    assert config_path is None
