# Author:UserA
# 发布订阅模型——订阅者
import pika

connection = pika.BlockingConnection(pika.ConnectionParameters(
    host='localhost'))
channel = connection.channel()

# exchange='liao' 保持发布者和订阅者的exchange交换器的名称一样。
# 注意rabbitmq版本上的区别，有的版本参数是type='fanout'，有的版本参数是exchange_type='fanout'
channel.exchange_declare(exchange='liao', exchange_type='fanout')

result = channel.queue_declare(exclusive=True,queue="")  # 不指定queue名字,rabbit会随机分配一个名字,exclusive=True会在使用此queue的消费者断开后,自动将queue删除
queue_name = result.method.queue
print("自动生成的queue的名字为： ", queue_name)
# channel.queue_bind(exchange='liao',queue=queue_name)
channel.queue_bind(queue=queue_name,exchange='liao')

print('Waiting for exchange liao message：......')

def callback(ch, method, properties, body):
    print(" 订阅到的消息是： %r" % body)

# channel.basic_consume(callback,queue=queue_name,no_ack=True )
# 千万注意这里rabbitmq各个版本之间的参数名称和顺序不一样，注意区别，根据报错提示自行调整即可。
channel.basic_consume(on_message_callback=callback,queue=queue_name )

channel.start_consuming()
