
import pika
import time

def receive_messages(queue_name):
    # Create a connection to RabbitMQ
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()

    # Declare the queue (ensure it exists)
    channel.queue_declare(queue=queue_name, durable=True)

    while True:
        # Use basic_get to check for messages without blocking
        method_frame, header_frame, body = channel.basic_get(queue_name)

        if method_frame:
            # A message was received
            print("Received:", body.decode())
            # Acknowledge the message
            channel.basic_ack(method_frame.delivery_tag)
        else:
            # No message available
            print("No messages available. Polling again...")

        # Sleep for a short time to avoid busy waiting
        time.sleep(1)

    # Close connection (you can implement graceful shutdown)
    connection.close()

# Call the function with your queue name
receive_messages('your_queue_name')
