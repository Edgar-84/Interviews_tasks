import os
import pika
import json
import time
import uuid
from config import settings


def get_file_data(path_file: str) -> str:
    with open(path_file) as file:
        result = file.read()
    
    return result


def get_data_from_folder(path_folder: str) -> dict:
    name_files = [file for file in os.listdir(path_folder)]
    name_files = [os.path.join(path_folder, file_name) for file_name in name_files]
    data = list(map(get_file_data, name_files))
    
    return data


def send_data(work_time:int = 150):

    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    channel.exchange_declare(
        exchange='order',
        exchange_type='direct'
    )

    print('Starting sent messages. To exist CTRL + C')
    try:
        while True:
            time.sleep(15)
            result = get_data_from_folder(settings.path_data)

            order = {
                'id': str(uuid.uuid4()),
                'data': result
                }
            
            channel.basic_publish(
                exchange='order',
                routing_key='order.notify',
                body=json.dumps({'id': order['id'], 'data': order['data']})
            )

            channel.basic_publish(
                exchange='order',
                routing_key='order.report',
                body=json.dumps(order)
            )
    
    except KeyboardInterrupt:
        print('\nStopping sending messages')

    finally:
        connection.close()


if __name__ == '__main__':
    send_data()
