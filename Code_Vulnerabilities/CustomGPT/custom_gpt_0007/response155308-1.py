
import pika
import time

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (ensure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Attempt to get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # A message was retrieved
            print("Received message:", body.decode())
        else:
            # No message available
            print("No messages available, checking again...")

        # Sleep for a short period to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Receiver stopped.")

finally:
    # Clean up and close the connection
    connection.close()
