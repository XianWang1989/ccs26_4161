
import pika
import time

# Define parameters for RabbitMQ
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Attempt to get a message from the queue, do not block
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print("Received message:", body)
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages in the queue. Waiting...")

        # Sleep before polling again to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Polling stopped.")

finally:
    # Clean up the connection
    if connection.is_open:
        connection.close()
