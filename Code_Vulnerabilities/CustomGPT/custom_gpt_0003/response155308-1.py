
import pika
import time

# Define RabbitMQ connection parameters
parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(parameters)
channel = connection.channel()

# Declare the queue you want to listen to
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Use basic_get to check if there's a message available
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            # If a message was retrieved, process it
            print("Received message:", body.decode())
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            # If no message is available, you can perform other tasks or sleep
            print("No messages available, checking again...")

        # Sleep for a short while to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Consumer stopped.")
finally:
    # Make sure to close the connection
    connection.close()
