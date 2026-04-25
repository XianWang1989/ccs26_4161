
import pika
import time

# Set up connection parameters
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)

# Create a channel
channel = connection.channel()

# Declare the queue (ensure it exists)
queue_name = 'your_queue'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages without blocking
        method_frame, header_frame, body = channel.basic_get(queue_name, auto_ack=True)

        if method_frame:
            # A message was received
            print(f"Received message: {body.decode()}")
        else:
            # No message received, can perform other tasks if needed
            print("No messages available, doing other work...")

        # Wait a bit before polling again to avoid too tight of a loop
        time.sleep(1)

except KeyboardInterrupt:
    print("Receiver stopped by user.")
finally:
    # Cleanup
    channel.close()
    connection.close()
