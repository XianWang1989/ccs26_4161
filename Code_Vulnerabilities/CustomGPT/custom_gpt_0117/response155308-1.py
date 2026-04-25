
import pika
import time

# Set up the connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure the queue exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Attempt to get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue_name, auto_ack=True)

        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages available, waiting...")

        # Sleep for a bit before polling again to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping consumer...")
finally:
    # Clean up and close the connection
    connection.close()
