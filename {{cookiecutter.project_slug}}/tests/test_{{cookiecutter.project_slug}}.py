# -*- coding: utf-8 -*-

"""
    Tests for the `/{{ cookiecutter.project_slug }}.py` module.
"""

from unittest.mock import patch
from pathlib import Path
import sys

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


def test_locate_config_file(tmpdir):
    """
        Test the priority of the paths when locating the
        configuration file.
    """
    config_path = app.locate_config_file("my_test_app")
    assert config_path is None
    first_file = tmpdir.join("my_test_app.toml")
    second_file = tmpdir.mkdir("TMP").join("my_test_app.toml")
    first_file.write("-")
    second_file.write("-")
    first_file_parent = str(Path(first_file).parent) + "/"
    second_file_parent = str(Path(second_file).parent) + "/"
    config_path = app.locate_config_file(
        "my_test_app",
        locations=[
            first_file_parent,
            second_file_parent,
        ]
    )
    assert config_path == str(first_file)
    first_file.remove()
    config_path = app.locate_config_file(
        "my_test_app",
        locations=[
            first_file_parent,
            second_file_parent,
        ]
    )
    assert config_path == str(second_file)
    second_file.remove()
    config_path = app.locate_config_file(
        "my_test_app",
        locations=[
            first_file_parent,
            second_file_parent,
        ]
    )
    assert config_path is None
