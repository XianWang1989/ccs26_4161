
import pika
import time

# Set up connection parameters
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

        if method_frame:
            # We have a message
            print(f"Received message: {body.decode()}")
        else:
            # No messages available
            print("No messages. Waiting before checking again.")

        # Sleep for a bit before checking again to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping consumer.")
finally:
    # Clean up the connection
    connection.close()
