
import pika
import time

# Set up the connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'your_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Fetch a single message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            # If a message is returned, process it
            print(f"Received message: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        else:
            # No message available
            print("No messages in queue.")

        # Sleep for a moment
        time.sleep(1)  # Adjust the polling interval as needed

except KeyboardInterrupt:
    print("Shutting down...")

finally:
    # Ensure that you close the connection
    connection.close()
