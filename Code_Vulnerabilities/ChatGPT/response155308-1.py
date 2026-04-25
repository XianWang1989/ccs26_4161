
import pika
import time

# Set up RabbitMQ connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue you want to consume messages from
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Using basic_get to check for messages in a non-blocking way
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # If there is a message, process it
            print("Received message:", body.decode())
        else:
            # No messages available, you can perform other tasks if needed
            print("No messages, doing other work...")

        # Sleep for a while before checking again to reduce CPU usage
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping the consumer...")

finally:
    # Clean up and close the connection
    connection.close()
