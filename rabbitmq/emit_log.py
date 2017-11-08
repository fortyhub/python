#!/usr/bin/env python
import pika
import sys

username = 'rabbitmq'
password = 'rabbitmq'
credentials = pika.PlainCredentials(username, password)

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.18.5',credentials=credentials,port=5672))
channel = connection.channel()

channel.exchange_declare(exchange='logs',type='fanout')

message = ''.join(sys.argv[1:]) or "info: Hello World!"
channel.basic_publish(exchange='logs',routing_key='',body=message)

print " [x] Sent %r" % (message)
connection.close()
