# -*- coding: utf-8 -*-

"""
    Module containing the different views of the application.
"""

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def view_slash(request: Request) -> Response:
    """
        Server endpoint for `/`.

        :param request: Client's request
        :type request: Request
        :return: Server's response
        :rtype: Response
    """

    del request  # unused
    return web.Response(text="It works!")
