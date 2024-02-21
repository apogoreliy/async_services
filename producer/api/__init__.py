import logging
import os

from aiohttp import web

from api.services.handler import Handler


def main():
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.INFO
    )

    app = web.Application()
    app.add_routes([
        web.get('/', Handler.health_status),
        web.post('/', Handler.publish),
    ])

    web.run_app(
        app,
        port=int(os.environ.get("SERVER_PORT"))
    )
