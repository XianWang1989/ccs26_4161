
import pika
import time

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue from which to consume
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Use basic_get to check for messages
        method_frame, header_frame, body = channel.basic_get(queue_name)

        if method_frame:
            # A message was received
            print("Received:", body.decode())
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            # No message was available
            print("No messages, checking again...")

        # Sleep for a short time to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Polling stopped.")

finally:
    # Cleanup
    connection.close()
