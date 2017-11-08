#!/usr/bin/env python
import pika
import sys

username = 'rabbitmq'
password = 'rabbitmq'
credentials = pika.PlainCredentials(username, password)

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.18.5',credentials=credentials,port=5672))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs',type='topic')

routing_key = sys.argv[1] if len(sys.argv) > 1 else 'anonymous.info'
message = ' '.join(sys.argv[2:]) or "Hello World!"
channel.basic_publish(exchange='topic_logs',routing_key=routing_key,body=message)

print " [x] Sent %r:%r" % (routing_key,message)
connection.close()
