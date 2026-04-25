
import pika
import time

# Set up the connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            # If we received a message, process it
            print(f"Received message: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        else:
            # No messages were available
            print("No messages available, checking again in 1 second...")

        # Sleep to prevent busy-waiting
        time.sleep(1)
except KeyboardInterrupt:
    print("Shutting down...")
finally:
    connection.close()
