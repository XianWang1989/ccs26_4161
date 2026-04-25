
import pika
import time

# Set up RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Get a message from the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        # Check if a message was received
        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages available")

        # Sleep for a bit to avoid busy-waiting
        time.sleep(1)

finally:
    # Close the connection when done
    connection.close()
