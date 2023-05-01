import os
import time
import json
import pika
from config import settings


def callback(ch, method, properties, body):
    info = json.loads(body)
    time.sleep(35)

    with open(f"{os.path.join(settings.path_result_files, info['id'])}.txt", 'w+') as new_file:
            file_info = '\n'.join(info['data'])
            new_file.write(file_info)
    
    for file in os.listdir(settings.path_data):
        os.remove(os.path.join(settings.path_data, file))
    
    ch.basic_ack(delivery_tag=method.delivery_tag)


def start_listening():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    queue = channel.queue_declare('order_notify')
    queue_name = queue.method.queue

    channel.queue_bind(
        exchange='order',
        queue=queue_name,
        routing_key='order.notify'
    )

    print('Waiting for messages. To exist CTRL + C')
    channel.basic_consume(on_message_callback=callback, queue=queue_name)
    
    try:
        channel.start_consuming()
    except KeyboardInterrupt:
        print('\nStopping waiting messages')


if __name__ == '__main__':
     start_listening()
