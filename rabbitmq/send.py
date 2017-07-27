#!/usr/bin/env python
import pika

username = 'rabbitmq'
password = 'rabbitmq'

credentials = pika.PlainCredentials(username, password)

connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.18.5', credentials=credentials, port=5672))

channel = connection.channel()
channel.queue_declare(queue='hello')
channel.basic_publish(exchange='',routing_key='hello',body='Hello World!')

print " [x] Sent 'Hello World!'"

connection.close()
