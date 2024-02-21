from aiohttp import web

from api.lib.rabbitmq_server import RabbitmqServer


class Handler:
    @staticmethod
    async def publish(request):
        body = await request.json()
        rabbitmq = RabbitmqServer()
        rabbitmq.publish(message={"data": body})
        return web.json_response({'message': body})

    @staticmethod
    async def health_status(request):
        return web.json_response({'message': "UP"})
