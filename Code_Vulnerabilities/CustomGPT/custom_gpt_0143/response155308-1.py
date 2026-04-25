
import pika
import time

# Set up connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue you want to consume from
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No messages in queue, checking again...")

        # Sleep for a short period to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping the receiver.")

finally:
    # Clean up
    channel.close()
    connection.close()
