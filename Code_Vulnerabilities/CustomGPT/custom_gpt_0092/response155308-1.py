
import pika
import time

# Define the RabbitMQ connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)

# Create a channel
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Try to get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # A message was received
            print(f"Received message: {body.decode()}")
        else:
            # No message received
            print("No message available.")

        # Optionally, introduce a delay to avoid tight looping
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Close the connection
    connection.close()
