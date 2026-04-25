
import pika
import time

# Set up RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Try to get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # Message was received
            print("Received message:", body.decode())
        else:
            # No message received
            print("Waiting for messages...")

        # Sleep for a bit before checking again
        time.sleep(1)

except KeyboardInterrupt:
    print("Receiver stopped.")

finally:
    # Close the connection
    connection.close()
