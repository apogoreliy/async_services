import logging
import os

from aiohttp import web

from .gateway.rabbitmq import RabbitMQ
from .services.handler import Handler


async def health_status(request):
    return web.json_response({'message': "UP"})


def main():
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p',
        level=logging.INFO
    )

    rabbitmq_instance = RabbitMQ()
    app = web.Application()
    handler = Handler(rabbitmq_instance)

    app.add_routes([
        web.get('/', health_status),
        web.post('/', handler.publish),
    ])

    web.run_app(
        app,
        port=int(os.environ.get("SERVER_PORT"))
    )
