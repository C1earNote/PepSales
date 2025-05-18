import pika
import json
from app.notification_sender import send_notification  # You’ll write this

def callback(ch, method, properties, body):
    message = json.loads(body)
    print(f"Received message: {message}")
    send_notification(message)
    ch.basic_ack(delivery_tag=method.delivery_tag)

def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters("localhost"))
    channel = connection.channel()
    channel.queue_declare(queue="notifications", durable=True)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue="notifications", on_message_callback=callback)

    print("Worker started. Waiting for messages...")
    channel.start_consuming()

if __name__ == "__main__":
    main()
