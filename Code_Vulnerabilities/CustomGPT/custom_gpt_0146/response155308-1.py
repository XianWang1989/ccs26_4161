
import pika
import time

# Set up your RabbitMQ connection
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare your queue (make sure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Check for messages in the queue
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            # A message is available
            print("Received message:", body.decode())

            # Acknowledge the message to remove it from the queue
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No messages available. Checking again...")

        # Sleep for a bit before checking again
        time.sleep(1)

except KeyboardInterrupt:
    print("Exiting...")
finally:
    connection.close()
