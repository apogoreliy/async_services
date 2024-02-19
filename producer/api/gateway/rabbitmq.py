import json
import os
import logging

import pika


class RabbitMQ:
    def __init__(self):
        self._queue = os.environ.get("RABBITMQ_QUEUE")
        self._host = os.environ.get("RABBITMQ_HOST")
        self._routing_key = os.environ.get("RABBITMQ_ROUTING_KEY")
        self._exchange = os.environ.get("RABBITMQ_EXCHANGE")
        self._username = os.environ.get("RABBITMQ_USERNAME")
        self._password = os.environ.get("RABBITMQ_PASSWORD")
        self.start_server()

    def start_server(self):
        self.create_channel()
        self.create_exchange()
        self.create_bind()
        logging.info("Channel created...")

    def create_channel(self):
        credentials = pika.PlainCredentials(username=self._username, password=self._password)
        parameters = pika.ConnectionParameters(self._host, virtual_host="/", credentials=credentials)
        self._connection = pika.BlockingConnection(parameters)
        self._channel = self._connection.channel()

    def create_exchange(self):
        self._channel.exchange_declare(
            exchange=self._exchange,
            exchange_type='direct',
            passive=False,
            durable=True,
            auto_delete=False
        )
        self._channel.queue_declare(queue=self._queue, durable=False)

    def create_bind(self):
        self._channel.queue_bind(
            queue=self._queue,
            exchange=self._exchange,
            routing_key=self._routing_key
        )

    def publish(self, message={}):
        """
        :param message: message to publish in JSON format
        """

        self._channel.basic_publish(
            exchange=self._exchange,
            routing_key=self._routing_key,
            body=json.dumps(message),
            properties=pika.BasicProperties(content_type='application/json')
        )
        logging.info("Published Message: {}".format(message))
