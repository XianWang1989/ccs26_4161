
import pika
import time

# Setup RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
channel.queue_declare(queue='your_queue_name')

try:
    while True:
        # Attempt to get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue='your_queue_name')

        if method_frame:
            # If a message was returned, process it
            print(f"Received message: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        else:
            # No message was received
            print("No message available, waiting...")

        # Sleep for a bit to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Receiver stopped.")

finally:
    # Cleanup
    connection.close()
