
import pika
import time

# Set up the connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare your queue (make sure it exists)
queue_name = 'your_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Poll for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No messages available. Waiting...")

        # Sleep for a bit before checking again
        time.sleep(1)

finally:
    connection.close()
