
import pika
import time

# Set up connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure the queue exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to poll for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages available")

        # Sleep for a while to avoid busy-waiting
        time.sleep(1)
finally:
    # Clean up
    connection.close()
