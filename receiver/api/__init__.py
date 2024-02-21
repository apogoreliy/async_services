import logging

from api.lib.rabbitmq_server import RabbitmqServer


def main():
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO
    )

    server = RabbitmqServer()
    server.get_messages()
