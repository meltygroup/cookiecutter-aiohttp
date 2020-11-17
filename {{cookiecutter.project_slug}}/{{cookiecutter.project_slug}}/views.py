"""Module containing the different views of the application.
"""

from aiohttp import web
from aiohttp.web_request import Request
from aiohttp.web_response import Response


async def view_slash(request: Request) -> Response:
    """Server endpoint for `/`.
    """

    del request  # unused
    return web.Response(text="It works!")
