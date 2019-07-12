# Author:UserA
# rabbitmq 消费者
import pika
import time

connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()
channel.queue_declare(queue='hello3', durable=True)  # durable=True只是帮队列名称持久化，并不是将消息持久化。

# 在各个消费者端，配置perfetch=1,就是告诉RabbitMQ在这个消费者当前消息还没处理完的时候就不要再发新消息
channel.basic_qos(prefetch_count=1)

def callback(ch, method, properties, body):
    print("---->", ch, method, property)
    # time.sleep(20)
    print("Received %r" % body)
    ch.basic_ack(delivery_tag=method.delivery_tag)

# channel.basic_consume(callback, queue='hello1', no_ack=True) #这是老版本参数的顺序
# 修改参数顺序
'''
把
chan.basic_consume(callback, queue='hello', no_ack=True)
改成
chan.basic_consume(queue='hello', on_message_callback=callback, auto_ack=True)
就好了 是源码里面参数的位置变了
'''
channel.basic_consume(
    'hello3',
    callback,
    # auto_ack=True #true代表不用确认，false代表要需要客户端确认。
)

print('Waiting for messages.....')
channel.start_consuming()
