#!/usr/bin/env python
import sys
import pika

username = 'rabbitmq'
password = 'rabbitmq'

message = ''.join(sys.argv[1:]) or "Hello World!"

credentials = pika.PlainCredentials(username, password)

connection = pika.BlockingConnection(pika.ConnectionParameters(
                                        host='192.168.18.5', 
                                        credentials=credentials,
                                        port=5672))

channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
channel.basic_publish(exchange='',routing_key='task_queue',
                      body=message,
                      properties=pika.BasicProperties(delivery_mode = 2))

print " [x] Sent %r" %(message,)

connection.close()
