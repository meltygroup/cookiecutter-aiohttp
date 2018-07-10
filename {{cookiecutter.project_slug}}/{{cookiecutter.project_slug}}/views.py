# -*- coding: utf-8 -*-

"""
    Module containing the different views of the application.
"""

from aiohttp import web
from aiohttp.web_response import Response


async def view_slash() -> Response:
    """
        Server endpoint for `/`.

        :return: Server's response
        :rtype: Response
    """

    return web.Response(text="It works!")
