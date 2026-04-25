
import pika
import time

# Set up the connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        # Check if a message was received
        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No message available, waiting...")

        # Optionally sleep to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Consumer stopped by user.")
finally:
    # Clean up the connection
    connection.close()
