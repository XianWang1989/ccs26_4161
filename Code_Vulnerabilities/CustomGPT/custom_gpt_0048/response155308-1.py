
import pika
import time

# Set up connection parameters
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # Message available
            print(f"Received message: {body.decode()}")
        else:
            # No message available
            print("No message available.")

        # Sleep for a short time to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped by user.")
finally:
    connection.close()
