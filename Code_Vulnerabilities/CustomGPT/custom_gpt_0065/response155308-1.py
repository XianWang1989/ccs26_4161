
import pika
import time

# Connection setup
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
queue_name = 'your_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Non-blocking get call
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print("Received message:", body.decode())
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No message available, checking again...")

        # Sleep to avoid tight loop
        time.sleep(1)

finally:
    connection.close()
