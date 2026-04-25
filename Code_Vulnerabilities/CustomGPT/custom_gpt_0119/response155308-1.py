
import pika
import time

# Set up connection parameters
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (ensure it exists)
channel.queue_declare(queue='your_queue_name')

try:
    while True:
        # Try to get a message from the queue (non-blocking)
        method_frame, header_frame, body = channel.basic_get(queue='your_queue_name', auto_ack=True)

        # Check if a message was received
        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No messages available, checking again...")

        # Sleep for a while before checking again to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Interrupted by user")

finally:
    # Clean up and close the connection
    channel.close()
    connection.close()
