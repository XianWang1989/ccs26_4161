
import pika
import time

# Establish a connection to RabbitMQ
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name, durable=True)

while True:
    # Use basic_get to retrieve a message without blocking
    method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

    if method_frame:
        print("Received message:", body.decode())
    else:
        print("No message available, checking again...")

    # Sleep for a short duration to avoid busy-waiting
    time.sleep(1)

# Close the connection (this will never be reached in this example)
# connection.close()
