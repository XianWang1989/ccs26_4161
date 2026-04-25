
import pika
import time

# Set up a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'your_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Attempt to get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            # Message was returned from the queue
            print(f"Received message: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            # No message available, sleep for a bit before the next check
            print("No messages, checking again...")

        # Sleep briefly to avoid busy-waiting
        time.sleep(1)

finally:
    # Close the connection
    connection.close()
