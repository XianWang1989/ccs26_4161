
import pika
import time

# Set up connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure it exists)
channel.queue_declare(queue='your_queue_name')

try:
    while True:
        # Use basic_get to check for messages non-blocking
        method_frame, header_frame, body = channel.basic_get(queue='your_queue_name')

        if method_frame:
            print("Received message:", body)
            # Acknowledge the message
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        else:
            print("No message available, waiting...")

        # Sleep for a short duration before polling again
        time.sleep(1)

finally:
    connection.close()
