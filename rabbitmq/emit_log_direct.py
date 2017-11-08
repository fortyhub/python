#!/usr/bin/env python
import pika
import sys

username = 'rabbitmq'
password = 'rabbitmq'
credentials = pika.PlainCredentials(username, password)

connection = pika.BlockingConnection(pika.ConnectionParameters(
        host='192.168.18.5',credentials=credentials,port=5672))
channel = connection.channel()

channel.exchange_declare(exchange='direct_logs',type='direct')

severity = sys.argv[1] if len(sys.argv) > 1 else 'info'
message = ' '.join(sys.argv[2:]) or "info: Hello World!"
channel.basic_publish(exchange='direct_logs',routing_key=severity,body=message)

print " [x] Sent %r:%r" % (severity,message)
connection.close()
