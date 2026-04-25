
import pika
import time

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Attempt to get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # If a message was received
            print(f"Received message: {body.decode()}")
        else:
            # No message available; wait before polling again
            print("No message available. Checking again...")

        # Sleep for a short period to avoid tight loop
        time.sleep(1)

finally:
    # Clean up and close the connection
    connection.close()
