# Credit - adarsh-goel

from aiohttp import web
from .route import routes


web_app = web.Application()
web_app.add_routes(routes)
