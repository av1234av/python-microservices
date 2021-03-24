# amqps://fitqdpae:YO54htaZ5wRA_kTSt73mKKTIyvmaAHjG@coyote.rmq.cloudamqp.com/fitqdpae

import pika
import json
from pika.spec import Queue

params = pika.URLParameters('amqps://fitqdpae:YO54htaZ5wRA_kTSt73mKKTIyvmaAHjG@coyote.rmq.cloudamqp.com/fitqdpae')

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)