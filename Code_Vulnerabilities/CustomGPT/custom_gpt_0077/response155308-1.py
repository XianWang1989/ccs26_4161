
import pika
import time

# Set up connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (optional but recommended)
queue_name = 'my_queue'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Check for messages without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            # A message is available
            print("Received message:", body.decode())
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            # No message available
            print("No messages in the queue.")

        # Sleep for a while before checking again
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping the consumer.")

finally:
    connection.close()
