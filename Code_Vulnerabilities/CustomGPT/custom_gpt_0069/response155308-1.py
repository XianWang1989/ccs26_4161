
import pika
import time

# Setup connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure it matches the sender's queue)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print(f"Received message: {body.decode()}")
            channel.basic_ack(method_frame.delivery_tag)  # Acknowledge the message
        else:
            print("No messages in the queue.")

        time.sleep(1)  # Polling interval
finally:
    connection.close()
