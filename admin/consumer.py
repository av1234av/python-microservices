# amqps://fitqdpae:YO54htaZ5wRA_kTSt73mKKTIyvmaAHjG@coyote.rmq.cloudamqp.com/fitqdpae

import pika
import json
import os
import django
from pika.spec import Queue
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "admin.settings")
django.setup()

from products.models import Product

params = pika.URLParameters('amqps://fitqdpae:YO54htaZ5wRA_kTSt73mKKTIyvmaAHjG@coyote.rmq.cloudamqp.com/fitqdpae')

connection = pika.BlockingConnection(params)

channel = connection.channel()
channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print("recieved in admin")
    id = json.loads(body)
    print(id)
    product = Product.objects.get(id=id)
    product.likes = product.likes + 1
    product.save()
    print('Product likes increased')

channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()