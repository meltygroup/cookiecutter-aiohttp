# -*- coding: utf-8 -*-

"""
    Application entry point.
"""

from pathlib import Path
from typing import Union
import sys
import argparse
import logging
import toml
from aiohttp import web
import logger
import views


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
    parser.add_argument(
        "-v",
        "--verbose",
        action="store_true",
        dest="verbose",
        default=False,
        help="enable debug logs",
    )
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


def create_app(log: logging.Logger, config: dict) -> web.Application:
    """
        Function who create the aiohttp web application.

        :param log: Instance of the logger to use
        :type log: logging.Logger
        :param config: Parsed configuration file
        :type config: dict
        :return: Instance of the aiohttp web application
        :rtype: web.Application
    """

    app = web.Application()
    app["logger"] = log
    app["config"] = config
    app.router.add_get("/", views.view_slash)
    return app


if __name__ == "__main__":
    LOG = logger.get_logger("{{ cookiecutter.project_slug }}")
    ARGS = parse_args()

    if ARGS.config is not None:
        CONFIG_PATH = ARGS.config
    else:
        CONFIG_PATH = locate_config_file("{{ cookiecutter.project_slug }}")
        if CONFIG_PATH is None:
            LOG.error("Failed to find the configuration file for the app, exiting.")
            sys.exit(1)

    LOG.debug("Configuration path is %s.", CONFIG_PATH)
    CONFIG = toml.load(CONFIG_PATH)
    APP = create_app(LOG, CONFIG)
    web.run_app(APP, host=CONFIG["server"]["host"], port=CONFIG["server"]["port"])
    LOG.info(
        "Server running on %s:%d.", CONFIG["server"]["host"], CONFIG["server"]["port"]
    )
