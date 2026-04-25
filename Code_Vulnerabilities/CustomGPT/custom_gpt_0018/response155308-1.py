
import pika
import time

# Set up the connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure it exists beforehand)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Getting the message without blocking
        method_frame, header_frame, body = channel.basic_get(queue_name, auto_ack=True)

        # Check if a message was returned
        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages available.")

        # Sleep for a short time to prevent a busy loop
        time.sleep(1)

finally:
    # Clean up and close the connection
    connection.close()
