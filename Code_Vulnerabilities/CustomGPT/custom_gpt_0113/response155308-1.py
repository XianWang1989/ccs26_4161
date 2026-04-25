
import pika
import time

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Check for messages in the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:  # If a message is available
            print("Received message:", body)
            # Acknowledge message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available. Waiting...")

        # Sleep for a bit to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Consumer stopped.")
finally:
    # Close the connection
    connection.close()
