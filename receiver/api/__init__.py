import logging

from .gateway.rabbitmq import RabbitmqServer


def main():
    logging.basicConfig(
        format='%(asctime)s %(message)s',
        datefmt='%m/%d/%Y %I:%M:%S %p', level=logging.INFO
    )

    server = RabbitmqServer()
    server.get_messages()
