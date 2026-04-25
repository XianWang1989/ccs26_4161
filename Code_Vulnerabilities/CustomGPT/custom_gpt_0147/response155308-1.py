
import pika
import time

# Establish connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue to consume from
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Check for messages without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            # Process the message
            print("Received message:", body.decode())
        else:
            print("No messages available. Waiting...")

        # Sleep for a short period to avoid busy-waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")

finally:
    # Clean up and close the connection
    connection.close()
