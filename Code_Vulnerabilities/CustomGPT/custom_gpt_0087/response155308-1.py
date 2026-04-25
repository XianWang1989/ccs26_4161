
import pika
import time

# Set up the connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No messages available. Waiting before checking again...")

        # Sleep for a while to avoid busy waiting
        time.sleep(1)

finally:
    connection.close()
