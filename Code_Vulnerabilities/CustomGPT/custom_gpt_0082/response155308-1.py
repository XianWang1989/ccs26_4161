
import pika
import time

# Set up connection parameters
connection_params = pika.ConnectionParameters(
    host='localhost'
)

# Create a connection and a channel
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Check for messages without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # Process the message
            print("Received message:", body.decode())
        else:
            print("No messages available.")

        # Sleep for a short period to avoid busy waiting
        time.sleep(1)

finally:
    # Close the connection gracefully
    connection.close()
