import pika, json

def send_to_queue(notification_data: dict):
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    channel.queue_declare(queue='notifications')

    channel.basic_publish(
        exchange='',
        routing_key='notifications',
        body=json.dumps(notification_data)
    )

    connection.close()
