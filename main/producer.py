# amqps://fitqdpae:YO54htaZ5wRA_kTSt73mKKTIyvmaAHjG@coyote.rmq.cloudamqp.com/fitqdpae

import pika
import os
import json
from pika.spec import Queue

AMQP_URI=os.environ['AMQP_URI']
params = pika.URLParameters(AMQP_URI)

connection = pika.BlockingConnection(params)

channel = connection.channel()

def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='admin', body=json.dumps(body), properties=properties)