
import pika
import time

# Set up your RabbitMQ connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Try to get a message without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print("Received message:", body.decode())
            # Acknowledge the message so it's not re-queued
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No message available. Waiting before the next check...")

        # Wait for a bit before checking again to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Consumer stopped.")

finally:
    # Close the connection gracefully
    connection.close()
