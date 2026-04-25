
import pika
import time

# Set up connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue
channel.queue_declare(queue='your_queue_name', durable=True)

try:
    while True:
        # Use basic_get to check for a message
        method_frame, header_frame, body = channel.basic_get(queue='your_queue_name', auto_ack=True)

        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No message available, polling...")

        # Sleep for a short period to avoid busy-waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping...")
finally:
    # Clean up
    connection.close()
