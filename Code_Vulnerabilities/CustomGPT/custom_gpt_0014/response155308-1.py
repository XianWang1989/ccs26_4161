
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
        # Attempt to get a message
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # Message found
            print(f"Received message: {body.decode()}")
        else:
            # No message available
            print("No messages in queue, waiting...")

        # Sleep before next check to prevent busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping the consumer...")
finally:
    # Clean up
    connection.close()
