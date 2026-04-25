
import pika
import time

# Connect to RabbitMQ server
connection = pika.BlockingConnection(pika.ConnectionParameters(host='localhost'))
channel = connection.channel()

# Declare the queue (make sure it matches the producer's queue)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Attempt to fetch a message
        method_frame, header_frame, body = channel.basic_get(queue_name)

        if method_frame:
            print("Received message:", body)
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available, checking again...")

        # Sleep for a short duration to avoid busy waiting
        time.sleep(1)

finally:
    # Close the connection
    connection.close()
