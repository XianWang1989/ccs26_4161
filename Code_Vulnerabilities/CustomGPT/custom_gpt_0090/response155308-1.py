
import pika
import time

# Setup connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Try to get a message without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print(f"Received message: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available, waiting...")

        # Sleep for a bit to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping consumer...")

finally:
    connection.close()
