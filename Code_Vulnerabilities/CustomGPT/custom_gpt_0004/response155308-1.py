
import pika
import time

# Set up connection parameters
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to retrieve a message (non-blocking)
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            # Process the message
            print(f"Received message: {body.decode()}")
            # Acknowledge message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available. Checking again...")

        # Optional: sleep for a while before checking again
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopped receiving messages.")

finally:
    # Clean up
    connection.close()
