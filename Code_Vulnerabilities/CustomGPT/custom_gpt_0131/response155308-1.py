
import pika
import time

# Set up connection parameters
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# Declare the queue
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Check for messages without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print(f"Received message: {body.decode()}")
            # Process your message here

        else:
            print("No messages available. Checking again...")

        # Sleep for a short time to avoid busy-waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Receiver stopped.")

finally:
    connection.close()
