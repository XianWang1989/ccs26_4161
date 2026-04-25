
import pika
import time

# Set up the connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print("Received message:", body)
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available. Waiting...")

        # Sleep for a short period to avoid busy-waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    # Cleanup
    connection.close()
