
import pika
import time

# Define connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue if it doesn't exist
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print("Received message:", body.decode())
            # Acknowledge the message
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        else:
            print("No messages available. Checking again in 1 second...")

        # Sleep briefly to avoid busy waiting
        time.sleep(1)
except KeyboardInterrupt:
    print("Exiting...")
finally:
    # Clean up and close the connection
    connection.close()
