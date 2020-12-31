import pika

params = pika.URLParameters('amqps://zkniapmf:lrFY0tV1m0hP1MuuxawNXAZV_HAO2ER7@rattlesnake.rmq.cloudamqp.com/zkniapmf')

connection = pika.BlockingConnection(params)

channel = connection.channel()

channel.queue_declare(queue='admin')

def callback(ch, method, properties, body):
    print('Received in admin')
    print(body)


channel.basic_consume(queue='admin', on_message_callback=callback, auto_ack=True)

print('Started Consuming')

channel.start_consuming()

channel.close()