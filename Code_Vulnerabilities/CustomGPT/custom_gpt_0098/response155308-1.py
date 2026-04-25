
import pika
import time

# Setup connection to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue from which you want to consume messages
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print("Received message:", body.decode())
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available. Waiting...")

        # Sleep for a while to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Consumer stopped.")

finally:
    # Clean up and close the connection
    connection.close()
