
import pika
import time

# Define connection parameters
connection_params = pika.ConnectionParameters(host='localhost')

# Establish a connection and create a channel
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare your queue (make sure it exists)
queue_name = 'your_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Fetch a single message without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print(f"Received message: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No message available; sleeping for a while...")

        # Sleep for a short amount of time to prevent busy waiting
        time.sleep(1)

finally:
    # Cleanly close the connection
    connection.close()
