import pika,json

params = pika.URLParameters('amqps://zkniapmf:lrFY0tV1m0hP1MuuxawNXAZV_HAO2ER7@rattlesnake.rmq.cloudamqp.com/zkniapmf')

connection = pika.BlockingConnection(params)

channel = connection.channel()




def publish(method, body):
    properties = pika.BasicProperties(method)
    channel.basic_publish(exchange='', routing_key='main', body=json.dumps(body), properties=properties)

