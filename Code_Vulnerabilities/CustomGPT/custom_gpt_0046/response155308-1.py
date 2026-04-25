
import pika
import time

# Define connection parameters
credentials = pika.PlainCredentials('username', 'password')  # replace with your credentials
parameters = pika.ConnectionParameters('localhost', 5672, '/', credentials)

# Create a new connection and channel
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare the queue (optional, based on your setup)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue_name)

        if method_frame:
            print(f"Received message: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available.")

        time.sleep(1)  # Delay to prevent tight loop
except KeyboardInterrupt:
    print("Stopping receiver...")
finally:
    connection.close()
