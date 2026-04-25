
import pika
import time

# Set up connection parameters
connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

while True:
    # Use basic_get to check for messages
    method_frame, header_frame, body = channel.basic_get(queue=queue_name)

    if method_frame:
        # If a message is available, process it
        print("Received message:", body.decode())

        # Acknowledge the message
        channel.basic_ack(delivery_tag=method_frame.delivery_tag)
    else:
        # No message available
        print("No messages, waiting...")

    # Sleep for a while before checking again
    time.sleep(1)

# Close the connection (will not be reached in this loop)
# connection.close()
