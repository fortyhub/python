#!/usr/bin/env python
import time
import pika

username = 'rabbitmq'
password = 'rabbitmq'

credentials = pika.PlainCredentials(username, password)
connection = pika.BlockingConnection(pika.ConnectionParameters(
                    host='192.168.18.5', credentials=credentials, port=5672))
        
channel = connection.channel()
channel.queue_declare(queue='task_queue', durable=True)
        
print ' [*] Waiting for messages. To exit press CTRL+C'
        
def callback(ch, method, properties, body):
    print " [x] Received %r" % (body,)
    time.sleep( body.count('.'))
    print " [x] Done"
    ch.basic_ack(delivery_tag = method.delivery_tag)

channel.basic_qos(prefetch_count=1)
channel.basic_consume(callback,queue='task_queue')
channel.start_consuming()
