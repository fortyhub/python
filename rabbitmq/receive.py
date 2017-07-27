#!/usr/bin/env python
import pika

username = 'rabbitmq'
password = 'rabbitmq'

credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(pika.ConnectionParameters(host='192.168.18.5', credentials=credentials, port=5672))
        
channel = connection.channel()
channel.queue_declare(queue='hello')
        
print ' [*] Waiting for messages. To exit press CTRL+C'
        
def callback(ch, method, properties, body): print " [x] Received %r" % (body,)

channel.basic_consume(callback,queue='hello',no_ack=True)
channel.start_consuming()
