
import pika
import time

# Set up the connection and channel
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Declare the queue (make sure it exists)
queue_name = 'your_queue_name'
channel.queue_declare(queue=queue_name)

try:
    while True:
        # Poll for messages without blocking
        method_frame, header_frame, body = channel.basic_get(queue=queue_name, auto_ack=True)

        if method_frame:
            print(f"Received message: {body.decode()}")
        else:
            print("No messages in queue.")

        # Sleep for a short time to avoid busy waiting
        time.sleep(1)

except KeyboardInterrupt:
    print("Stopping the consumer.")

finally:
    connection.close()
