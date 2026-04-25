
import pika
import time

# Define the RabbitMQ connection parameters
connection_parameters = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_parameters)
channel = connection.channel()

# Declare the queue (ensure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Poll for a message
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No messages available.")

        # Sleep for a short duration to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print('Polling stopped.')

finally:
    connection.close()
