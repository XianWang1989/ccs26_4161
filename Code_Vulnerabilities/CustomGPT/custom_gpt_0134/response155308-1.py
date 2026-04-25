
import pika
import time

# RabbitMQ connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue to consume from
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

while True:
    # Use basic_get to check for messages
    method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

    if method_frame:
        # If a message is returned, process it
        print(f"Received message: {body.decode()}")
    else:
        # No messages available
        print("No messages to process. Waiting...")

    # Sleep for a bit before polling again to prevent busy-waiting
    time.sleep(2)  # Adjust the sleep time as needed

# Close the connection when done (not reachable in this example)
# connection.close()
