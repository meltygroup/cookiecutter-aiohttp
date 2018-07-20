# -*- coding: utf-8 -*-

"""
    Application entry point.
"""

from pathlib import Path
from typing import Union
import sys
import argparse
import toml
from aiohttp import web

import {{ cookiecutter.project_slug }}.views as views


def parse_args(program_args=None) -> argparse.Namespace:
    """
        Parse command line arguments.

        :param program_args: Arguments of the program
        :type program_args: list of str
        :return: The argparse's parsed arguments
        :rtype: argparse.Namespace
    """

    if program_args is None:
        program_args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", dest="config", help="path to the config file")
    return parser.parse_args(program_args)


def locate_config_file(app_name: str, locations=None) -> Union[str, None]:
    """
        Function who locate the config file between multiple paths.

        :param app_name: Name of the application
        :type app_name: str
        :return: Path to the config file or None if not found
        :rtype: str
    """
    if locations is None:
        locations = ["./", "~/", "~/.config/", "/etc/"]

    for location in locations:
        full_path = location + app_name + ".toml"
        if Path(full_path).is_file():
            return full_path
    return None


def create_app(config: dict) -> web.Application:
    """
        Function who create the aiohttp web application.

        :param config: Parsed configuration file
        :type config: dict
        :return: Instance of the aiohttp web application
        :rtype: web.Application
    """

    app = web.Application()
    app["config"] = config
    app.router.add_get("/", views.view_slash)
    return app


def main(program_args=None):  # pragma: no cover
    """
        Main entry point of the program

        :param program_args: Arguments of the program (defaults to sys.argv)
        :type program_args: list of str
    """
    args = parse_args(program_args)

    if args.config is not None:
        config_path = args.config
    else:
        config_path = locate_config_file("{{ cookiecutter.project_slug }}")
        if config_path is None:
            print("Failed to find the configuration file for the app, exiting.")
            sys.exit(1)

    config = toml.load(config_path)
    app = create_app(config)
    web.run_app(app, host=config["server"]["host"], port=config["server"]["port"])
