"""{{ cookiecutter.project_name }} entry point.
"""

from pathlib import Path
from typing import Union, Optional, Dict, Any
import logging
import sys
import argparse
import toml
from aiohttp import web

import {{ cookiecutter.project_slug }}.views as views


def parse_args(program_args=None) -> argparse.Namespace:
    """Parse command line arguments.
    """

    if program_args is None:
        program_args = sys.argv[1:]

    parser = argparse.ArgumentParser()
    parser.add_argument("-c", "--config", dest="config", help="path to the config file")
    return parser.parse_args(program_args)


def locate_config_file(app_name: str, locations=None) -> Union[str, None]:
    """Function who locate the config file between multiple paths.
    """
    if locations is None:
        locations = ["./", "~/", "~/.config/", "/etc/"]

    for location in locations:
        full_path = location + app_name + ".toml"
        if Path(full_path).is_file():
            return full_path
    return None


def create_app(config: Optional[Dict[str, Any]] = None) -> web.Application:
    """Build an aiottp server instance to serve {{ cookiecutter.project_name }}.
    """
    if config is None:
        config = load_config()
    app = web.Application()
    app["config"] = config
    app.router.add_get("/", views.view_slash)
    return app


def load_config(config_path=None) -> Dict[str, Any]:
    """Find a config file and load it."""
    if config_path is None:  # pragma: no cover
        config_path = locate_config_file("{{ cookiecutter.project_slug }}")
        if config_path is None:
            print("Failed to find {{ cookiecutter.project_name }}'s configuration.",
                  "exiting.", file=sys.stderr)
            sys.exit(1)

    with open(config_path) as config_file:
        return toml.load(config_file)


def main(program_args=None):  # pragma: no cover
    """Start a {{ cookiecutter.project_name }} server."""
    args = parse_args(program_args)
    logging.basicConfig(level=logging.DEBUG)
    config = load_config(args.config)
    app = create_app(config)
    web.run_app(app, host=config["server"]["host"], port=config["server"]["port"])
