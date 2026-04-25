
import pika
import time

# Set up connection parameters
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue you want to consume from
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

try:
    while True:
        # Use basic_get to retrieve a message without blocking
        method_frame, header_frame, body = channel.basic_get(queue_name)

        if method_frame:
            print(f"Received message: {body}")
            # Acknowledge the message after processing
            channel.basic_ack(method_frame.delivery_tag)
        else:
            print("No message available, waiting...")

        # Sleep for a bit before checking again to avoid busy loop
        time.sleep(1)

except KeyboardInterrupt:
    print("Interrupted!")
finally:
    connection.close()
