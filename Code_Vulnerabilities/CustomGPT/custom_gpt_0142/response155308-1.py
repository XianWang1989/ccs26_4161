
import pika
import time

# Set up the connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

# Create a channel
channel = connection.channel()

# Declare the queue (ensure it exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Try to get a message from the queue without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # If a message is received, process it
            print(f"Received message: {body.decode()}")
        else:
            # No message received; you can add logic here if needed
            print("No messages in the queue. Checking again...")

        # Sleep for a little while to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping the consumer.")
finally:
    # Clean up
    connection.close()
