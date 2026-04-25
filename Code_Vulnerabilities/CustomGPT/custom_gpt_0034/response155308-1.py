
import pika
import time

# Connection parameters
connection_params = pika.ConnectionParameters('localhost')
connection = pika.BlockingConnection(connection_params)
channel = connection.channel()

# Declare the queue (make sure the queue exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Check for messages in a non-blocking way
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print("Received message:", body.decode())
        else:
            print("No message available, checking again...")

        # Sleep for a bit to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping the consumer...")
finally:
    channel.close()
    connection.close()
