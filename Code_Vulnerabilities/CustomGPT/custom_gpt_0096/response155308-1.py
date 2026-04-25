
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
        # Check for messages without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print("Received message:", body.decode())
            # Acknowledge message
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        else:
            print("No messages available.")

        # Sleep for a short period to avoid busy waiting
        time.sleep(1)

finally:
    connection.close()
