# Author:UserA
# 发布订阅模型——发布者
import pika
import sys

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

# exchange='liao' 保持发布者和订阅者的exchange交换器的名称一样。
# channel.exchange_declare(exchange='liao', type='fanout')
# 注意rabbitmq版本上的区别，有的版本参数是type='fanout'，有的版本参数是exchange_type='fanout'
channel.exchange_declare(exchange='liao', exchange_type='fanout')

# message = ' '.join(sys.argv[1:]) or "info: Hello World!"
message = "info: Hello World!2222"
channel.basic_publish(exchange='liao',
                      routing_key='',
                      body=message)
print("Sent message： %r" % message)
connection.close()
