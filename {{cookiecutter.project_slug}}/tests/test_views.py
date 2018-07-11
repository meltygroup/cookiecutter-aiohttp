# -*- coding: utf-8 -*-

"""
    Tests for the `/views.py` module.
"""

import logging
import toml
import pytest
import {{ cookiecutter.project_slug }} as app
import logger


@pytest.fixture
def client(loop, aiohttp_client):
    """
        Create a test web server.
    """
    logging.raiseExceptions = False
    log = logger.get_logger("{{ cookiecutter.project_slug }}")
    config = toml.load("tests/test_server_config.toml")
    web_app = app.create_app(log, config)
    return loop.run_until_complete(aiohttp_client(web_app))


async def test_view_slash(client):
    """
        Test the response of `GET /`.
    """
    response = await client.get('/')
    assert response.status == 200
    assert await response.text() == "It works!"
