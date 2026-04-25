
import pika
import time

# Set up the connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue
queue_name = 'your_queue'
channel.queue_declare(queue=queue_name, durable=True)

while True:
    # Use basic_get to check for messages
    method_frame, header_frame, body = channel.basic_get(queue=queue_name)

    if method_frame:
        print("Received message:", body.decode())
        # Acknowledge the message
        channel.basic_ack(method_frame.delivery_tag)
    else:
        print("No messages available. Checking again...")

    # Wait before checking again to avoid busy-waiting
    time.sleep(1)  # Adjust the sleep time as necessary

# Close the connection
connection.close()
