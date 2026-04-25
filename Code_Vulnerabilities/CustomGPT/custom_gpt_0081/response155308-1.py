
import pika
import time

# Set up connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Try to get a message without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # A message was received
            print("Received message:", body.decode())
        else:
            # No message received, wait before checking again
            print("No messages available. Retrying in 1 second...")

        # Sleep for a short duration to prevent busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Interrupted, stopping the consumer...")

finally:
    # Clean up
    connection.close()
