
import pika
import time

# Connection parameters
connection_params = pika.ConnectionParameters(host='localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Make sure the queue exists
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Check for a message without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name)

        if method_frame:
            print(f"Received message: {body.decode()}")
            # Acknowledge the message
            channel.basic_ack(delivery_tag=method_frame.delivery_tag)
        else:
            print("No messages available.")

        # Sleep for a while to avoid busy-waiting
        time.sleep(1)

finally:
    connection.close()
