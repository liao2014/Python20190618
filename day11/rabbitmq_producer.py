# Author:UserA
# rabbitmq 生产者
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# 声明queue
channel.queue_declare(queue='hello3', durable=True)  # durable=True只是帮队列名称持久化，并不是将消息持久化。

# n RabbitMQ a message can never be sent directly to the queue, it always needs to go through an exchange.
channel.basic_publish(exchange='',
                      routing_key='hello3',
                      body='Hello World3333!',
                      properties=pika.BasicProperties(
                         delivery_mode = 2 # make message persistent  将消息持久化。
                      )
                      )
print("Sent 'Hello World3333!'")
connection.close()
